"""
Vented enclosure: a fixed CAD artifact published to MakerRepo.com.

An *artifact* is a CAD model produced by a single function. When you push your
repo to MakerRepo.com, CI runs this function, exports the geometry (STEP, STL,
etc.), and attaches it to the build so you can view and share it in the web UI.

Use the @artifact decorator from the makerrepo library (imported as `mr`) on
any function that returns a Build123D Build (or equivalent) result.
"""
from build123d import Axis
from build123d import Box
from build123d import BuildPart
from build123d import fillet
from build123d import Locations
from build123d import Mode
from mr import artifact


# The @artifact decorator registers this function so that:
# - MakerRepo.com: when you push, CI runs vented_enclosure(), exports
#   geometry (STEP, STL, 3MF, etc.), and attaches it to the build for
#   viewing/sharing in the web UI.
# - MakerRepo CLI (mr): use `mr artifacts list`, `mr artifacts view`,
#   `mr artifacts export`, `mr artifacts snapshot` to work with this
#   model locally.
# Docs: https://docs.makerrepo.com/artifacts/
@artifact(
    cover=True,
    short_desc="Small vented enclosure with rounded corners — sample artifact",
    export_step=True,
    export_3mf=True,
)
def vented_enclosure():
    """
    A small enclosure (e.g. for a tiny electronics project) with vent slots
    and filleted edges.

    The function must return the BuildPart context manager's result so MakerRepo
    can export the solid. Use cover=True to use this model's snapshot as the
    repository cover image on MakerRepo.com.
    """
    with BuildPart() as build:
        # Base box: 60×40×25 mm
        Box(60, 40, 25)
        # Round the top edges for a friendlier look (fillet radius 3 mm)
        # Box is centered so Z runs from -12.5 to 12.5; top edges are near Z=12.5
        top_edges = build.edges().filter_by_position(Axis.Z, 10, 15)
        fillet(top_edges, radius=3)
        # Vent slots on the two long sides: cut small rectangular openings
        slot_w, slot_h = 8, 4
        slot_spacing = 12
        for side in (-1, 1):
            y_pos = side * (40 / 2 - 2)  # inset slightly from outer face
            for i in range(4):
                x_pos = -60 / 2 + slot_spacing + i * (slot_w + slot_spacing)
                with Locations((x_pos, y_pos, 25 / 2)):
                    Box(slot_w, 3, slot_h, mode=Mode.SUBTRACT)
    return build
