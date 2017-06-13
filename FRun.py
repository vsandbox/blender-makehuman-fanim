import bpy
from mathutils import Vector
from FReload import FReload

FReload.reload(["FAnimator", "FBone", "FRun", "FTracker", "FUtil", "FBoundaries"])
from FAnimator import FAnimator
from FBone import FSimpleBone, FRotationBone
from FBoundaries import FBoundaries

class FRun:
    @staticmethod
    def run(s_object_name: str = "Girl1"):
        print("\n\n------- Start facial animation\n----------------------------------\n")
        animator = FAnimator(bpy.context.scene, {
            "frame_init": 20,
            "s_object_name": s_object_name,
            "bones": [
                {
                    "type": FSimpleBone,
                    "bones": ["jaw"],
                    "trackers": ["trk_chin.M"],
                    "factors": [Vector((0, 0, 0.2))],
                    "boundaries": [FBoundaries(Vector((0, 0, -0.005)), Vector((0, 0, -0.08)))]
                },

                # Lip Corners
                {
                    "type": FSimpleBone,
                    "bones": ["levator05.R"],
                    "trackers": ["trk_lip.RC"],
                    "factors": [Vector((0.1, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0.1, 0, 0.5)), Vector((-0.5, 0, -0.5)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["levator04.R"],
                    "trackers": ["trk_lip.RC"],
                    "factors": [Vector((0.3, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0.02, 0, 0.1)), Vector((0, 0, -0.1)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["levator05.L"],
                    "trackers": ["trk_lip.LC"],
                    "factors": [Vector((0.1, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0.5, 0, 0.5)), Vector((-0.5, 0, -0.5)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["levator04.L"],
                    "trackers": ["trk_lip.LC"],
                    "factors": [Vector((-0.3, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0.02, 0, 0.1)), Vector((-0.8, 0, -0.1)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["risorius03.R"],
                    "trackers": ["trk_lip.RC"],
                    "factors": [Vector((0.1, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0.5, 0, 0.5)), Vector((-0.5, 0, -0.5)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["temporalis02.R"],
                    "trackers": ["trk_lip.RC"],
                    "factors": [Vector((0.05, 0, 0.05))],
                    "boundaries": [FBoundaries(Vector((0.5, 0, 0.5)), Vector((-0.5, 0, -0.5)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["risorius03.L"],
                    "trackers": ["trk_lip.LC"],
                    "factors": [Vector((0.1, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0.5, 0, 0.5)), Vector((-0.5, 0, -0.5)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["temporalis02.L"],
                    "trackers": ["trk_lip.LC"],
                    "factors": [Vector((0.05, 0, 0.05))],
                    "boundaries": [FBoundaries(Vector((0.5, 0, 0.5)), Vector((-0.5, 0, -0.5)))]
                },

                # Lip Top
                {
                    "type": FSimpleBone,
                    "bones": ["special01"],
                    "trackers": ["trk_lip.TM"],
                    "factors": [Vector((0, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0, 0, 0.02)), Vector((0, 0, 0.05)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["oris04.R"],
                    "trackers": ["trk_lip.TR"],
                    "factors": [Vector((0.1, 0, 0))],
                    "boundaries": [FBoundaries(Vector((0.2, 0, 0)), Vector((-0.2, 0, 0)))]
                },
                # {
                #     "type": FSimpleBone,
                #     "bones": ["oris04.L"],
                #     "trackers": ["trk_lip.TL"],
                #     "factors": [Vector((0.1, 0, 0))],
                #     "boundaries": [FBoundaries(Vector((0.5, 0, 0.5)), Vector((-0.5, 0, 0.05)))]
                # },

                # Lip Bottom
                {
                    "type": FSimpleBone,
                    "bones": ["oris01"],
                    "trackers": ["trk_lip.BM"],
                    "factors": [Vector((0, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0, 0, 0)), Vector((0, 0, -0.05)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["oris07.R"],
                    "trackers": ["trk_lip.BR"],
                    "factors": [Vector((0.1, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0.05, 0, 0.05)), Vector((-0.05, 0, -0.05)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["oris07.L"],
                    "trackers": ["trk_lip.BL"],
                    "factors": [Vector((0.1, 0, 0.1))],
                    "boundaries": [FBoundaries(Vector((0.05, 0, 0.05)), Vector((-0.05, 0, -0.05)))]
                },

                # Brow Right
                {
                    "type": FSimpleBone,
                    "bones": ["oculi02.R"],
                    "trackers": ["trk_brow.RM"],
                    "factors": [Vector((0, 0, 0.05))],
                    "boundaries": [FBoundaries(Vector((0, 0, 0.05)), Vector((0, 0, -0.05)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["temporalis01.R"],
                    "trackers": ["trk_brow.RR"],
                    "factors": [Vector((0.1, 0, 0.01))],
                    "boundaries": [FBoundaries(Vector((0.05, 0, 0.001)), Vector((-0.05, 0, -0.001)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["oculi01.R"],
                    "trackers": ["trk_brow.RL"],
                    "factors": [Vector((0.1, 0, 0.01))],
                    "boundaries": [FBoundaries(Vector((0.05, 0, 0.01)), Vector((-0.05, 0, -0.01)))]
                },

                # Brow Left
                {
                    "type": FSimpleBone,
                    "bones": ["oculi02.L"],
                    "trackers": ["trk_brow.LM"],
                    "factors": [Vector((0, 0, 0.05))],
                    "boundaries": [FBoundaries(Vector((0, 0, 0.05)), Vector((0, 0, -0.05)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["temporalis01.L"],
                    "trackers": ["trk_brow.LR"],
                    "factors": [Vector((0.1, 0, 0.01))],
                    "boundaries": [FBoundaries(Vector((0.05, 0, 0.001)), Vector((-0.05, 0, -0.001)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["oculi01.L"],
                    "trackers": ["trk_brow.LL"],
                    "factors": [Vector((0.1, 0, 0.01))],
                    "boundaries": [FBoundaries(Vector((0.05, 0, 0.01)), Vector((-0.05, 0, -0.01)))]
                },

                # Nose
                {
                    "type": FSimpleBone,
                    "bones": ["levator06.R"],
                    "trackers": ["trk_nose.R"],
                    "factors": [Vector((0.02, 0, 0.04))],
                    "boundaries": [FBoundaries(Vector((0.05, 0, 0.05)), Vector((-0.05, 0, -0.05)))]
                },
                {
                    "type": FSimpleBone,
                    "bones": ["levator06.L"],
                    "trackers": ["trk_nose.L"],
                    "factors": [Vector((0.02, 0, 0.04))],
                    "boundaries": [FBoundaries(Vector((0.05, 0, 0.05)), Vector((-0.05, 0, -0.05)))]
                },

                # Head
                {
                    "type": FSimpleBone,
                    "bones": ["head"],
                    "trackers": ["trk_chin.M"],
                    "factors": [Vector((0.05, 0, 0.05))],
                    "boundaries": [FBoundaries(Vector((0.2, 0, 0.2)), Vector((-0.2, 0, -0.2)))]
                }
            ]
        })

        animator.init()
        animator.start()
