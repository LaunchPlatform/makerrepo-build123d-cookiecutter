"""
Sample generator: a parametric CAD model users can customize on MakerRepo.com.

A *generator* is a parametric model: a function that takes user-supplied
parameters (defined with Pydantic) and returns a customized Build123D object.
On MakerRepo.com, visitors can tweak parameters in the web UI and request
a new build. Use @customizable and a Pydantic model for parameters.
"""
from build123d import Box
from build123d import Build
from build123d import Mode
from build123d import Pos
from mr import customizable
from pydantic import BaseModel
from pydantic import Field


class DeskOrganizerParameters(BaseModel):
    """Parameters for the desk organizer. Each field becomes a control in the MakerRepo UI."""

    length: float = Field(default=120.0, gt=0, description="Overall length (X) in mm")
    width: float = Field(default=80.0, gt=0, description="Overall width (Y) in mm")
    height: float = Field(default=35.0, gt=0, description="Wall height in mm")
    wall_thickness: float = Field(
        default=2.0, ge=1.0, lt=10.0, description="Wall and divider thickness in mm"
    )
    n_length: int = Field(
        default=3, ge=1, le=8, description="Number of compartments along length"
    )
    n_width: int = Field(
        default=2, ge=1, le=6, description="Number of compartments along width"
    )


@customizable(
    sample_parameters=DeskOrganizerParameters(
        length=120,
        width=80,
        height=35,
        wall_thickness=2,
        n_length=3,
        n_width=2,
    ),
    short_desc="Parametric desk organizer — compartments, size, and wall thickness",
)
def desk_organizer(parameters: DeskOrganizerParameters):
    """
    Build a desk organizer tray with a configurable grid of compartments.

    sample_parameters is used to build a preview/snapshot shown on MakerRepo.com.
    When users change parameters and request a build, this function is called
    with their values. The function must accept a single `parameters` argument
    and return a Build123D object (Compound or Solid).
    """
    L = parameters.length
    W = parameters.width
    H = parameters.height
    t = parameters.wall_thickness
    nx = parameters.n_length
    ny = parameters.n_width

    with Build() as build:
        # Outer tray (hollow box: base and four walls)
        Box(L, W, H)
        # Hollow out the inside
        with Pos(0, 0, t):
            Box(L - 2 * t, W - 2 * t, H - t + 0.1, mode=Mode.SUBTRACT)

        # X-direction dividers (span full width, run along Y)
        cell_l = (L - (nx - 1) * t) / nx
        for i in range(nx - 1):
            x = -L / 2 + (i + 1) * cell_l + (i + 0.5) * t
            with Pos(x, 0, H / 2):
                Box(t, W - 2 * t, H + 0.1, mode=Mode.ADD)

        # Y-direction dividers (span full length, run along X)
        cell_w = (W - (ny - 1) * t) / ny
        for j in range(ny - 1):
            y = -W / 2 + (j + 1) * cell_w + (j + 0.5) * t
            with Pos(0, y, H / 2):
                Box(L - 2 * t, t, H + 0.1, mode=Mode.ADD)

    return build
