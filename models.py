from typing import Optional
import torch
import torch.nn as nn
import torch.nn.functional as F

from torch import Tensor


class BrainAgeCNN(nn.Module):
    """
    The BrainAgeCNN predicts the age given a brain MR-image.
    """
    def __init__(self) -> None:
        super().__init__()

        # Feel free to also add arguments to __init__ if you want.
        # ----------------------- ADD YOUR CODE HERE --------------------------

        # ------------------------------- END ---------------------------------

    def forward(self, imgs: Tensor) -> Tensor:
        """
        Forward pass of your model.

        :param imgs: Batch of input images. Shape (N, 1, H, W, D)
        :return pred: Batch of predicted ages. Shape (N)
        """
        # ----------------------- ADD YOUR CODE HERE --------------------------
        pred = None
        # ------------------------------- END ---------------------------------
        return pred

    def train_step(
        self,
        imgs: Tensor,
        labels: Tensor,
        return_prediction: Optional[bool] = False
    ):
        """Perform a training step. Predict the age for a batch of images and
        return the loss.

        :param imgs: Batch of input images (N, 1, H, W, D)
        :param labels: Batch of target labels (N)
        :return loss: The current loss, a single scalar.
        :return pred
        """
        pred = self(imgs)  # (N)

        # ----------------------- ADD YOUR CODE HERE --------------------------
        loss = None
        # ------------------------------- END ---------------------------------

        if return_prediction:
            return loss, pred
        else:
            return loss
