import bpy
from mathutils import Matrix, Vector
from FUtil import FUtil
from FTracker import FTracker
from FBoundaries import FBoundaries


class AFBone:
    """Abstract Bone Class"""

    def __init__(self, bones: list, trackers: list, factors: list, boundaries: list):
        self.bones = bones
        self.trackers = trackers
        self.factors = factors
        self.boundaries = boundaries

    def update(self):
        print("Not implemented update")

    def get_translation(self,
                        bone: bpy.types.PoseBone,
                        tracker: FTracker,
                        boundaries: FBoundaries,
                        v_factor: Vector = Vector((1, 1, 1)),
                        ):
        m_tracker_translation = boundaries.fix(tracker.get_translation_matrix(v_factor))
        m_reset = Matrix.Translation(bone.location).inverted()
        return FUtil.get_global_translation(bone.matrix * m_reset, m_tracker_translation)


class FSimpleBone(AFBone):
    """Translates two axis of single bone according to tracker"""

    def update(self):
        bone = self.bones[0]
        tracker = self.trackers[0]
        bone.matrix = self.get_translation(bone, tracker, self.boundaries[0], self.factors[0])

class FRotationBone(AFBone):

    def update(self):
        bone = self.bones[0]
        tracker = self.trackers[0]
        # self.get_translation(bone, tracker, self.boundaries[0], self.factors[0])
        bone.matrix = self.get_translation(bone, tracker, self.boundaries[0], self.factors[0])

    def get_translation(self,
                        bone: bpy.types.PoseBone,
                        tracker: FTracker,
                        boundaries: FBoundaries,
                        v_factor: Vector = Vector((1, 1, 1)),
                        ):
        m_tracker_translation = boundaries.fix(tracker.get_translation_matrix(v_factor))
        #angle = m_tracker_translation.to_translation().angle(tracker.m_start.to_translation())
        q_rotation = m_tracker_translation.to_translation().rotation_difference(tracker.m_start.to_translation())
        return q_rotation.to_matrix().to_4x4() * bone.matrix.to_quaternion().to_matrix().to_4x4().inverted()
        #print("\nangle\n", angle)
        #print("\ndiff\n", )