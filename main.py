from manim import *
import random 
import copy

class Compare1(Scene):
    def construct(self):
        grad_len = 40
        arr1 = [i for i in range(grad_len)]
        random.shuffle(arr1)
        arr2 = copy.deepcopy(arr1)
        reference_colors = [RED, YELLOW, BLUE]
        grad_colors = color_gradient(reference_colors, grad_len)
        grp1 = VGroup(*[Rectangle(width=0.25, height=2, fill_opacity=1, color=grad_colors[i]) for i in range(grad_len)])
        grp2 = VGroup(*[Rectangle(width=0.25, height=2, fill_opacity=1, color=grad_colors[i]) for i in range(grad_len)])
        grp1cpy = grp1.copy()
        grp2cpy = grp2.copy()
        grp1.arrange(buff=0.1)
        grp2.arrange(buff=0.1)
        grp1.shift(UP*5)
        grp2.shift(DOWN*3)
        bh = Text("Bubble Sort", font_size=86).shift(UP*7.5)
        sh = Text("Selection Sort", font_size=86).shift(DOWN*0.5)
        self.play(Create(grp1), Create(grp2), Write(bh), Write(sh), run_time=0.5)
        for i in range(grad_len):
            grp1cpy[i] = grp2cpy[arr1[i]]
        grp2cpy = grp1cpy.copy()
        grp1cpy.arrange(buff=0.1)
        grp2cpy.arrange(buff=0.1)
        grp1cpy.shift(UP*5)
        grp2cpy.shift(DOWN*3)
        self.play(ReplacementTransform(grp1, grp1cpy), ReplacementTransform(grp2, grp2cpy), run_time=0.2)
        bsqueue = []
        for i in range(grad_len-1):
            sorted = True 
            for j in range(grad_len-1-i):
                bsqueue.append({"op": "pos", "pos": j})
                if arr1[j] > arr1[j+1]:
                    bsqueue.append({"op": "swap", "pos":[j, j+1]})
                    tmp = arr1[j]
                    arr1[j] = arr1[j+1]
                    arr1[j+1] = tmp
                    sorted = False
            if sorted:
                bsqueue.append({"op": "sorted"})
                break
        if bsqueue[-1]["op"] != "sorted":
            bsqueue.append({"op": "sorted"})

        iqueue = []
        for i in range(grad_len-1):
            sorted = True
            minVal = arr2[i]
            minIdx = i
            for j in range(i+1, grad_len):
                iqueue.append({"op": "pos", "pos": j})
                if arr2[j] < minVal:
                    minIdx = j
                    minVal = arr2[j]
                    sorted = False

            tmp = arr2[i]
            arr2[i] = arr2[minIdx]
            arr2[minIdx] = tmp
            iqueue.append({"op": "swap", "pos":[i, minIdx]})
        if iqueue[-1]["op"] != "sorted":
            iqueue.append({"op": "sorted"})

        print(len(iqueue), len(bsqueue))
        c= 0
        g1ph =-1 
        g2ph =-1 
        while True:
            c += 1
            ag = []
            if len(bsqueue) == 0 and len(iqueue) == 0:
                break
            if len(bsqueue) > 0:
                if g1ph > -1:
                    ag.append(grp1[g1ph].animate.set(height=2.0))
                    ag.append(grp1[g1ph+1].animate.set(height=2.0))
                bsop = bsqueue[0]
                bsqueue = bsqueue[1:]
                if bsop["op"] == "pos":
                    ag.append(grp1[bsop["pos"]].animate.set(height=2.5))
                    ag.append(grp1[bsop["pos"]+1].animate.set(height=2.5))
                    g1ph = bsop["pos"]
                elif bsop["op"] == "swap":
                    p1 = bsop["pos"][0]
                    p2 = bsop["pos"][1]
                    ag.append(Swap(grp1[p1], grp1[p2]))
                    tmp = grp1[p1]
                    grp1[p1] = grp1[p2]
                    grp1[p2] = tmp
                elif bsop["op"] == "sorted":
                    ag.append(grp1[g1ph].animate.set(height=2.0))
                    ag.append(grp1[g1ph+1].animate.set(height=2.0))

            if len(iqueue) > 0:
                if g1ph > -1:
                    ag.append(grp2[g2ph].animate.set(height=2.0))
                bsop = iqueue[0]
                iqueue = iqueue[1:]
                if bsop["op"] == "pos":
                    ag.append(grp2[bsop["pos"]].animate.set(height=2.5))
                    g2ph = bsop["pos"]
                elif bsop["op"] == "swap":
                    p1 = bsop["pos"][0]
                    p2 = bsop["pos"][1]
                    ag.append(Swap(grp2[p1], grp2[p2]))
                    tmp = grp2[p1]
                    grp2[p1] = grp2[p2]
                    grp2[p2] = tmp
                elif bsop["op"] == "sorted":
                    ag.append(grp2[g2ph].animate.set(height=2.0))
            self.play(AnimationGroup(*ag), run_time = 0.025)

        self.wait(1)

def main():
    print("Hello from compsort1!")


if __name__ == "__main__":
    main()
