import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Display an STL in Genesis.")
    parser.add_argument("file", type=Path, help="Path to your .stl file")
    parser.add_argument("--scale", type=float, default=1.0)
    args = parser.parse_args()
    if not args.file.is_file() or args.file.suffix.lower() != ".stl":
        parser.error("Provide an existing .stl file.")
    if not 0 < args.scale < float("inf"):
        parser.error("Scale must be a positive, finite number.")

    # Genesis prints Unicode symbols that the default Windows encoding cannot handle.
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfigure):
        reconfigure(encoding="utf-8")
    import genesis as gs

    gs.init()
    scene = gs.Scene(
        show_viewer=True,
        viewer_options=gs.options.ViewerOptions(res=(960, 640)),
    )
    scene.add_entity(gs.morphs.Plane())
    print(f"Loading {args.file}")
    scene.add_entity(
        gs.morphs.Mesh(
            file=str(args.file.resolve()),
            pos=(0, 0, 0.5),
            scale=args.scale,
            fixed=False,
        )
    )
    scene.build()
    print("Viewer ready. Close the Genesis window or press Ctrl+C to stop.")
    try:
        while scene.viewer.is_alive():
            scene.step()
    except KeyboardInterrupt:
        pass
    finally:
        scene.destroy()


if __name__ == "__main__":
    main()
