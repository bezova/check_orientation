from collections import namedtuple

from iglovikov_helper_functions.dl.pytorch.utils import rename_layers
from timm import create_model as timm_create_model
from torch import nn
from torch.utils import model_zoo

model = namedtuple("model", ["url", "model"])

models = {
    "resnet18_2020-11-07": model(
        model=timm_create_model("swsl_resnet18", pretrained=False, num_classes=4),
        url="https://github.com/ternaus/check_orientation/releases/download/v0.0.1/2020-11-07_resnet18.zip",
    )
}


def create_model(model_name: str) -> nn.Module:
    model = models[model_name].model
    state_dict = model_zoo.load_url(models[model_name].url, progress=True, map_location="cpu")["state_dict"]
    state_dict = rename_layers(state_dict, {"model.": ""})
    model.load_state_dict(state_dict)
    return model
