"""Config parameters for YOLOv3 models."""


class ConfigYOLOV3ResNet18:
    """
    Config parameters for YOLOv3.

    Examples:
        ConfigYoloV3ResNet18.
    """
    img_shape = [352, 640]
    feature_shape = [32, 3, 352, 640]
    num_classes = 3
    nms_max_num = 50
    _NUM_BOXES = 50

    backbone_input_shape = [64, 64, 128, 256]
    backbone_shape = [64, 128, 256, 512]
    backbone_layers = [2, 2, 2, 2]
    backbone_stride = [1, 2, 2, 2]

    ignore_threshold = 0.5
    obj_threshold = 0.3
    nms_threshold = 0.4

    anchor_scales = [(5, 3), (10, 13), (16, 30), (33, 23), (30, 61), (62, 45), (59, 119), (116, 90), (156, 198)]
    out_channel = int(len(anchor_scales) / 3 * (num_classes + 5))