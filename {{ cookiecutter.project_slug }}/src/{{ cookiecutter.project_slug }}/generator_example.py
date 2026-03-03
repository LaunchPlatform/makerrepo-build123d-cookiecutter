"""
Sample generator: a parametric CAD model users can customize on MakerRepo.com.

A *generator* is a parametric model: a function that takes user-supplied
parameters (defined with Pydantic) and returns a customized Build123D object.
On MakerRepo.com, visitors can tweak parameters in the web UI and request
a new build. Use @customizable and a Pydantic model for parameters.
"""

from build123d import Box
from mr import customizable
from pydantic import BaseModel, Field


class BoxParameters(BaseModel):
    """Parameters for the parametric box. Each field becomes a control in the MakerRepo UI."""

    width: float = Field(default=20.0, gt=0, description="Width (X) in mm")
    depth: float = Field(default=15.0, gt=0, description="Depth (Y) in mm")
    height: float = Field(default=10.0, gt=0, description="Height (Z) in mm")


@customizable(
    sample_parameters=BoxParameters(width=20, depth=15, height=10),
    short_desc="Parametric box — width, depth, height in mm",
)
def parametric_box(parameters: BoxParameters):
    """
    Build a box with user-defined dimensions.

    sample_parameters is used to build a preview/snapshot shown on MakerRepo.com.
    When users change parameters and request a build, this function is called
    with their values. The function must accept a single `parameters` argument
    and return a Build123D object (here we return the Box directly; the library
    accepts Compound and similar types).
    """
    return Box(
        parameters.width,
        parameters.depth,
        parameters.height,
    )
