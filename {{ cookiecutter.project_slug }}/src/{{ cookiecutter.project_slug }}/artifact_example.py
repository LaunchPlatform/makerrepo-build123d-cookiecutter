"""
Sample artifact: a fixed CAD model published to MakerRepo.com.

An *artifact* is a CAD model produced by a single function. When you push your
repo to MakerRepo.com, CI runs this function, exports the geometry (STEP, STL,
etc.), and attaches it to the build so you can view and share it in the web UI.

Use the @artifact decorator from the makerrepo library (imported as `mr`) on
any function that returns a Build123D Build (or equivalent) result.
"""

from build123d import Build, Box
from mr import artifact


@artifact(
    cover=True,
    short_desc="Simple 10×10×10 mm cube — sample artifact",
    export_step=True,
    export_3mf=True,
)
def sample_cube():
    """
    A minimal artifact: a 10 mm cube.

    The function must return the Build context manager's result so MakerRepo
    can export the solid. Use cover=True to use this model's snapshot as the
    repository cover image on MakerRepo.com.
    """
    with Build() as build:
        Box(10, 10, 10)
    return build
