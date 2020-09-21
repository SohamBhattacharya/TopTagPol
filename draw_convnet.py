"""
Copyright (c) 2017, Gavin Weiguang Ding
All rights reserved.

Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
    may be used to endorse or promote products derived from this software
    without specific prior written permission.

4. URL: https://github.com/gwding/draw_convnet

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.
"""


import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()
import matplotlib
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

#matplotlib.pyplot.rc("text", usetex = True)
#matplotlib.rcParams["text.latex.preamble"] += [r"\usepackage{amsmath}"]
#matplotlib.rcParams["text.latex.preamble"] += [r"\usepackage{slashed}"]

NumDots = 4
NumConvMax = 8
NumFcMax = 20
White = 1.0
Light = 0.8
Medium = 0.6
Dark = 0.4
Darker = 0.25
Black = 0.


def add_layer(patches, colors, size=(24, 24), num=5,
              top_left=[0, 0],
              loc_diff=[3, -3],
              ):
    # add a rectangle
    top_left = np.array(top_left)
    loc_diff = np.array(loc_diff)
    loc_start = top_left - np.array([0, size[0]])
    for ind in range(num):
        patches.append(Rectangle(loc_start + ind * loc_diff, size[1], size[0]))
        if ind % 2:
            colors.append(Medium)
        else:
            colors.append(Light)


def add_layer_with_omission(patches, colors, 
                            layerColor = np.array([1, 1, 1]),
                            shape = "rect",
                            size=(24, 24),
                            num=5, num_max=8,
                            num_dots=4,
                            top_left=[0, 0],
                            loc_diff=[3, -3],
                            ):
    # add a rectangle
    top_left = np.array(top_left)
    loc_diff = np.array(loc_diff)
    loc_start = top_left - np.array([0, size[0]])
    this_num = min(num, num_max)
    start_omit = (this_num - num_dots) // 2
    end_omit = this_num - start_omit
    start_omit -= 1
    for ind in range(this_num):
        if (num > num_max) and (start_omit < ind < end_omit):
            omit = True
        else:
            omit = False

        if omit:
            patches.append(
                Circle(loc_start + ind * loc_diff + np.array(size) / 2, 0.5))
        else:
            
            if (shape == "circ") :
                
                patches.append(
                    Circle(
                        loc_start + ind * loc_diff + np.array(size) / 2,
                        1.5,
                    )
                )
            
            elif (shape == "rect") :
                
                patches.append(
                    Rectangle(
                        loc_start + ind * loc_diff,
                        size[1], size[0],
                    )
                )

        if omit:
            colors.append(Black*layerColor)
        elif ind % 2:
            colors.append(Medium*layerColor)
        else:
            colors.append(Light*layerColor)


def add_mapping(patches, colors, start_ratio, end_ratio, patch_size, ind_bgn,
                top_left_list, loc_diff_list, num_show_list, size_list):

    start_loc = top_left_list[ind_bgn] \
        + (num_show_list[ind_bgn] - 1) * np.array(loc_diff_list[ind_bgn]) \
        + np.array([start_ratio[0] * (size_list[ind_bgn][1] - patch_size[1]),
                    - start_ratio[1] * (size_list[ind_bgn][0] - patch_size[0])]
                   )




    end_loc = top_left_list[ind_bgn + 1] \
        + (num_show_list[ind_bgn + 1] - 1) * np.array(
            loc_diff_list[ind_bgn + 1]) \
        + np.array([end_ratio[0] * size_list[ind_bgn + 1][1],
                    - end_ratio[1] * size_list[ind_bgn + 1][0]])


    patches.append(Rectangle(start_loc, patch_size[1], -patch_size[0]))
    colors.append(Dark)
    patches.append(Line2D([start_loc[0], end_loc[0]],
                          [start_loc[1], end_loc[1]]))
    colors.append(Darker)
    patches.append(Line2D([start_loc[0] + patch_size[1], end_loc[0]],
                          [start_loc[1], end_loc[1]]))
    colors.append(Darker)
    patches.append(Line2D([start_loc[0], end_loc[0]],
                          [start_loc[1] - patch_size[0], end_loc[1]]))
    colors.append(Darker)
    patches.append(Line2D([start_loc[0] + patch_size[1], end_loc[0]],
                          [start_loc[1] - patch_size[0], end_loc[1]]))
    colors.append(Darker)



def label(xy, text, xy_off=[0, 4]):
    
    plt.text(
        xy[0] + xy_off[0],
        xy[1] + xy_off[1],
        text,
        family = "serif",
        size = 8,
        horizontalalignment = "center",
        #bbox=dict(facecolor='red', alpha=0.5)
    )


if __name__ == "__main__":
    
    fc_unit_size = 2
    
    layer_width_convLayer = 50
    layer_width_fcLayer = 40
    
    layerShift_x = +3
    layerShift_y = -3
    
    padding_x = 15
    padding_y = 5
    
    labelOffset_convLayer_x = +0
    labelOffset_convLayer_y = -85
    
    labelOffset_fcLayer_x = +0
    labelOffset_fcLayer_y = -85
    
    flag_omit = True
    
    patches = []
    colors = []
    
    fig, ax = plt.subplots()
    
    ############################
    # conv layers
    
    # [(depth, y, x)]
    dim_list = [(3, 50, 50), (50, 41, 41), (50, 20, 20), (30, 16, 16), (30, 8, 8), (10, 7, 7), (10, 3, 3)]
    size_list = [(ele[1], ele[2]) for ele in dim_list]
    num_list =  [ele[0] for ele in dim_list]
    layerColorList = [np.array([0, 1, 1]) if (iEle in [0, 2, 4]) else np.array([1, 1, 1]) for iEle in range(0, len(dim_list))]
    
    #x_diff_list = [0, layer_width_convLayer, layer_width_convLayer, layer_width_convLayer, layer_width_convLayer]
    #x_diff_list = [0] + [max(layer_width_convLayer] * (len(size_list) - 1)
    x_diff_list = [0] + [max(layer_width_convLayer, size_list[idx-1][1]+padding_x) for idx in range(1, len(size_list))]
    
    #text_list = ["Inputs"] + ["Feature\nmaps"] * (len(size_list) - 1)
    text_list = ["Input"] + [""] * (len(size_list) - 1)
    
    loc_diff_list = [[layerShift_x, layerShift_y]] * len(size_list)
    
    x_diff_cumsum = np.cumsum(x_diff_list)
    
    num_show_list = list(map(min, num_list, [NumConvMax] * len(num_list)))
    top_left_list = np.c_[np.cumsum(x_diff_list), np.zeros(len(x_diff_list))]
    
    #print top_left_list
    
    top_center_list = np.c_[
        [x_diff_cumsum[idx] + size_list[idx][1]/2.0 for idx in range(0, len(size_list))],
        np.zeros(len(x_diff_list))
    ]
    
    #print(top_left_list)
    #print(top_center_list)
    
    for ind in range(len(size_list)-1,-1,-1):
        if flag_omit:
            add_layer_with_omission(patches, colors,
                                    layerColor = layerColorList[ind],
                                    size=size_list[ind],
                                    num=num_list[ind],
                                    num_max=NumConvMax,
                                    num_dots=NumDots,
                                    top_left=top_left_list[ind],
                                    loc_diff=loc_diff_list[ind])
        else:
            add_layer(patches, colors, size=size_list[ind],
                        num=num_show_list[ind],
                        top_left=top_left_list[ind], loc_diff=loc_diff_list[ind])
        
        label(
            top_center_list[ind],
            text_list[ind] + "\n{}@{}x{}".format(num_list[ind], size_list[ind][0], size_list[ind][1])
        )
    
    ############################
    # in between layers
    #start_ratio_list = [[0.4, 0.5], [0.4, 0.8], [0.4, 0.5], [0.4, 0.8]]
    #end_ratio_list = [[0.4, 0.5], [0.4, 0.8], [0.4, 0.5], [0.4, 0.8]]
    patch_size_list = [(10, 10), (2, 2), (5, 5), (2, 2), (2, 2), (2, 2)]
    start_ratio_list = [[0.4, 0.8] if idx%2 else [0.4, 0.5] for idx in range(0, len(patch_size_list))]
    end_ratio_list = [[0.4, 0.8] if idx%2 else [0.4, 0.5] for idx in range(0, len(patch_size_list))]
    ind_bgn_list = range(len(patch_size_list))
    text_list = [
        "Convolution\n(ReLU)",
        "Max-pooling\n2x2 stride",
        "Convolution\n(ReLU)",
        "Max-pooling\n2x2 stride",
        "Convolution\n(ReLU)",
        "Max-pooling\n2x2 stride",
        "Flatten\n\n"
    ]
    
    bottom_center_list = np.c_[
        [top_center_list[idx][0] + min(dim_list[idx][0], NumConvMax-1)*layerShift_x for idx in range(0, len(size_list))],
        np.zeros(len(size_list))
    ]
    
    #print(bottom_center_list)
    
    for ind in range(len(patch_size_list)):
        add_mapping(
            patches,
            colors,
            start_ratio_list[ind],
            end_ratio_list[ind],
            patch_size_list[ind], ind,
            top_left_list,
            loc_diff_list,
            num_show_list,
            size_list
        )
            
        label(
            #top_left_list[ind],
            #top_center_list[ind],
            bottom_center_list[ind],
            text_list[ind] + "\n{}x{} kernel".format(patch_size_list[ind][0], patch_size_list[ind][1]),
            xy_off = [labelOffset_convLayer_x, labelOffset_convLayer_y],
        )
    
    if (len(text_list) == len(bottom_center_list)) :
        
        label(
            bottom_center_list[-1],
            text_list[-1],
            xy_off = [labelOffset_convLayer_x, labelOffset_convLayer_y],
        )
    
    
    ############################
    # fully connected layers
    size_list = [(fc_unit_size, fc_unit_size)] * 3
    num_list = [90, 50, 1]
    num_show_list = list(map(min, num_list, [NumFcMax] * len(num_list)))
    #x_diff_list = [sum(x_diff_list) + layer_width_fcLayer, layer_width_fcLayer, layer_width_fcLayer]
    x_diff_list = [sum(x_diff_list)+layer_width_fcLayer] + [layer_width_fcLayer] * (len(size_list) - 1)
    layerColorList = [np.array([1, 1, 0]) if (iEle in [0, 1]) else np.array([1, 0, 0]) for iEle in range(0, len(dim_list))]
    
    x_diff_cumsum = np.cumsum(x_diff_list)
    
    top_center_list = np.c_[
        [x_diff_cumsum[idx] + fc_unit_size/2.0 for idx in range(0, len(x_diff_list))],
        np.zeros(len(x_diff_list))
    ]
    
    top_left_list = np.c_[np.cumsum(x_diff_list), np.zeros(len(x_diff_list))]
    loc_diff_list = [[fc_unit_size, -fc_unit_size]] * len(top_left_list)
    text_list = [""] * (len(size_list) - 1) + ["Output"]
    
    for ind in range(len(size_list)):
        if flag_omit:
            add_layer_with_omission(
                patches,
                colors,
                shape = "circ",
                layerColor = layerColorList[ind],
                size=size_list[ind],
                num=num_list[ind],
                num_max=NumFcMax,
                num_dots=NumDots,
                top_left=top_left_list[ind],
                loc_diff=loc_diff_list[ind]
            )
        
        else:
            add_layer(patches, colors, size=size_list[ind],
                        num=num_show_list[ind],
                        top_left=top_left_list[ind],
                        loc_diff=loc_diff_list[ind])
        
        label(
            #top_left_list[ind],
            top_center_list[ind],
            text_list[ind] + "\n{}".format(num_list[ind])
        )
    
    text_list = [
        "",
        "Fully\nconnected\n(ReLU)",
        "Fully\nconnected\n(sigmoid)",
    ]
    
    bottom_center_list = np.c_[
        [top_center_list[idx][0] + min(dim_list[idx][0], NumFcMax-1)*fc_unit_size for idx in range(0, len(x_diff_list))],
        np.zeros(len(size_list))
    ]
    
    for ind in range(len(size_list)):
        
        label(
            top_left_list[ind],
            text_list[ind],
            xy_off = [labelOffset_fcLayer_x, labelOffset_fcLayer_y]
        )
    
    
    ############################
    for patch, color in zip(patches, colors):
        
        patch.set_color(color * np.ones(3))
        
        if isinstance(patch, Line2D):
            
            patch.set_linewidth(0.5)
            ax.add_line(patch)
            
        else:
            
            patch.set_edgecolor(Black * np.ones(3))
            patch.set_linewidth(0.5)
            ax.add_patch(patch)
    
    plt.axis("equal")
    plt.axis("off")
    
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])
    
    #plt.box(on = None)
    
    plt.margins(x = 0.01, y = 0.01)
    
    #plt.tight_layout()
    #plt.subplots_adjust(left = -1)
    
    #plt.show()
    
    #fig_w = 10.0
    #fig_w = int(np.ceil(10.0 * (len(dim_list)+len(num_list)) / 7.0 * layer_width / layer_width))
    fig_w = 1.0*(len(dim_list)+len(num_list))
    fig_h = 2.5
    
    fig.set_size_inches(fig_w, fig_h)
    
    fig_dir  = "plots/network_diagrams"
    fig_name = "CNN-1"
    
    os.system("mkdir -p %s" %(fig_dir))
    
    
    fig_ext  = ".pdf"
    fig_out = "%s/%s%s" %(fig_dir, fig_name, fig_ext)
    print("Saving as: %s" %(fig_out))
    
    fig.savefig(
        fig_out,
        bbox_inches = "tight",
        pad_inches = 0,
    )
    
    
    fig_ext  = ".png"
    fig_out = "%s/%s%s" %(fig_dir, fig_name, fig_ext)
    print("Saving as: %s" %(fig_out))
    
    fig.savefig(
        fig_out,
        bbox_inches = "tight",
        pad_inches = 0,
    )
