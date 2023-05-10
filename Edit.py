from pathlib import Path
import nibabel as nib
from PyQt5.QtGui import QPixmap, QMouseEvent


def on_mousePressEvent(self, event: QMouseEvent):
    # mask_data = nib.load(Path(self.mask_path)).get_fdata()
    # mask_data.mousePressEvent = self.on_mousePressEvent
    # 获取当前坐标
    pos = event.pos()
    x, y = pos.x(), pos.y()
    print(f"pos: {pos}")

    if self.mask_path != '':
        data_mask = nib.load(Path(self.mask_path))
        data2 = data_mask.get_fdata()
        img_height, img_width, _ = data2.shape
        # 计算相对坐标
        F_width = self.F.width()
        F_height = self.F.height()
        print(f"F:{F_width},{F_height} | img:{img_width},{img_height}")
        scale_x = img_width / F_width
        scale_y = img_height / F_height
        relative_x = int(event.x() * scale_x)
        relative_y = int(event.y() * scale_y)
        print(f"Relative point: x={relative_x},y={relative_y}")