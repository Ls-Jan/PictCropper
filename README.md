# PictCropper

<br>图片分割器，用于行列分割图片时使用，亦可作为图片裁剪器使用(但不方便就是了，毕竟裁剪出的文件还得重命名)
<br>双击运行【main.py】
<br>存在着部分缺陷：
<br>①、缩放的百分比是固定的，也就是在进行图片缩放时会有明显的不流畅感
<br>②、左侧的列表里判断图片的依据是“后缀名”(后来读到PNG文件时才意识到翻车，但懒得改了)

<br>你说这玩意儿有用吧，实际上也不怎么好用，当时做它出来是因为想分割一些图片的但网上各种找都没找到合适的工具(当时还没用gayhub，估计gayhub是有的)，然后花了大把的时间硬搓出来，但搓是搓出来的，用倒不怎么用...


<br>
<br>
<br>部分文件说明：
<br>【XJ_Tool.py】中存放着生成“马赛克背景”的代码
<br>【XJ_NumInput.py】实现数字输入，这控件说实话我觉得做得还算不错，还算挺好用
<br>【XJ_ColorChoose.py】实现颜色选择，这控件感觉一般般吧写的不好不坏，算是能用的程度
<br>【XJ_TreeView.py】实现列表显示。在要求不高的场景下还算好用（当然这个类可以继续扩展，只是目前来说够用所以就不作修改）
<br>【XJ_Rect.py】这纯粹是设计上的失误，不该设计出这个数据结构的。整出这玩意儿的代价就是我代码里和裁剪区相关的逻辑判断统统都变得复杂了起来
<br>【XJ_SampleCropper.py】是裸装的分割/裁剪器，如果想做个单纯的图片裁剪器的话可以单独拿出这个类并对其中的参数进行设置，
<br>    &emsp;&emsp;&emsp;该类有着一般裁剪器所需的功能(如自由/受限裁剪，滚轮缩放，裁剪区发生变化时发出信号等)，也算是写的不错的控件了，
<br>    &emsp;&emsp;&emsp;虽然基于设计不良的数据结构XJ_Rect让人有点恼火，但可以对【XJ_AbstractCropper.py】(抽象裁剪器，完成逻辑任务)动大刀来摆脱这个不良的数据结构


<br>
<br>
<br>


# 【运行结果】
![1](https://github.com/Ls-Jan/PictCropper/blob/main/RunningResult%5BPNG%5D/1.png)
![2](https://github.com/Ls-Jan/PictCropper/blob/main/RunningResult%5BPNG%5D/2.png)
![3](https://github.com/Ls-Jan/PictCropper/blob/main/RunningResult%5BPNG%5D/3.png)
![4](https://github.com/Ls-Jan/PictCropper/blob/main/RunningResult%5BPNG%5D/4.png)
![5](https://github.com/Ls-Jan/PictCropper/blob/main/RunningResult%5BPNG%5D/5.png)
![6](https://github.com/Ls-Jan/PictCropper/blob/main/RunningResult%5BPNG%5D/6.png)


