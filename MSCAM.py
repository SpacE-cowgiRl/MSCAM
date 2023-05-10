#这是一个样例，最终将会被多尺度神经网络算法替换
import nibabel as nib
import numpy as np
from pathlib import Path

def MSCAM(nii_path):
    # 加载nii文件
    nii_img = nib.load(Path(nii_path))
    nii_data = nii_img.get_fdata()

    # 事例方法：绘制线条——这里假设要在图像的第一张切片上绘制一条线，坐标为起点(10, 10)，终点(100, 100)
    x_start, y_start = 10, 10
    x_end, y_end = 100, 100
    nii_data[:, :, 0] = np.clip(nii_data[:, :, 0], 0, 1)  # 将图像的第一张切片限定在0和1之间
    nii_data[y_start:y_end, x_start:x_end, 0] = 1  # 绘制线条，将对应位置的像素值设为1

    # 保存修改后的nii文件,文件名为xxx_mask.nii，存储位置为原文件同文件夹下
    output_path = nii_path.replace(".nii", "_mask.nii")
    nii_mask = nib.Nifti1Image(nii_data, affine=nii_img.affine)
    nib.save(nii_mask, output_path)
