"""
Bracket from the build123d tutorial: a fixed CAD artifact published to MakerRepo.com.

An *artifact* is a CAD model produced by a single function. When you push your
repo to MakerRepo.com, CI runs this function, exports the geometry (STEP, STL,
etc.), and attaches it to the build so you can view and share it in the web UI.

Use the @artifact decorator from the makerrepo library (imported as `mr`) on
any function that returns a build123d Build (or equivalent) result.
"""
from build123d import *
from mr import artifact


# Based on the "Designing a Part in build123d" tutorial:
# https://build123d.readthedocs.io/en/latest/tutorial_design.html
@artifact(
    cover=True,
    short_desc="Bracket from build123d tutorial — sample artifact",
    export_step=True,
    export_3mf=True,
)
def tutorial_bracket() -> BuildPart:
    """
    A bracket part modeled following the build123d "Designing a Part" tutorial.

    The function returns the BuildPart context manager's result so MakerRepo
    can export the solid. With cover=True this model's snapshot can be used as
    the repository cover image on MakerRepo.com.
    """
    thickness = 3 * MM
    width = 25 * MM
    length = 50 * MM
    height = 25 * MM
    hole_diameter = 5 * MM
    bend_radius = 5 * MM
    fillet_radius = 2 * MM

    with BuildPart() as bracket:
        with BuildSketch() as sketch:
            with BuildLine() as profile:
                FilletPolyline(
                    (0, 0),
                    (length / 2, 0),
                    (length / 2, height),
                    radius=bend_radius,
                )
                offset(amount=thickness, side=Side.LEFT)
            make_face()
            mirror(about=Plane.YZ)

        extrude(amount=width / 2)
        mirror(about=Plane.XY)

        corners = bracket.edges().filter_by(Axis.X).group_by(Axis.Y)[-1]
        fillet(corners, fillet_radius)

        with Locations(bracket.faces().sort_by(Axis.X)[-1]):
            Hole(hole_diameter / 2)

        with BuildSketch(bracket.faces().sort_by(Axis.Y)[0]):
            SlotOverall(20 * MM, hole_diameter)
        extrude(amount=-thickness, mode=Mode.SUBTRACT)

    return bracket
