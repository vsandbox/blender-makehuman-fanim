import bpy
from FTracker import FTracker


class FAnimatorOptions:
    """Options for FAnimator"""

    def __init__(self, options: dict):
        self.frame_init = options["frame_init"]
        self.bones = options["bones"]
        self.s_object_name = options["s_object_name"]

    @staticmethod
    def create(options):
        if isinstance(options, FAnimatorOptions):
            return options
        return FAnimatorOptions(options)


class FAnimator:
    """"Main Animator Class"""

    def __init__(self, scene: bpy.types.Scene, options: FAnimatorOptions):
        self.scene = scene
        self.bones = []
        self.trackers = {}
        self.frame_last = 0
        self.options = FAnimatorOptions.create(options)

    # Init tracker start positions
    def init(self):
        self.create_bones()
        self.frame_set(self.options.frame_init)
        for tracker_name in self.trackers:
            self.trackers[tracker_name].init()
        self.frame_set_last()

    # Start animation
    def start(self):
        self.stop()
        self.update(self.scene)
        bpy.app.handlers.frame_change_post.append(self.update)

    # Stop animation
    def stop(self):
        bpy.app.handlers.frame_change_post.clear()

    # Update animation
    def update(self, scene: bpy.types.Scene):
        if scene.frame_current is self.frame_last:
            return

        print("\n---\nFrame: ", scene.frame_current, "\n")

        self.frame_last = scene.frame_current
        for bone in self.bones:
            bone.update()

    # Create bones from passed options
    def create_bones(self):
        bones = self.bones
        for bone in self.options.bones:
            bones.append(bone["type"](
                list(map(lambda bone_name:
                    self.scene.objects[self.options.s_object_name].pose.bones[bone_name], bone["bones"])),
                list(map(lambda tracker_name:
                    self.get_or_register_tracker(tracker_name), bone["trackers"])),
                bone["factors"],
                bone["boundaries"]
            ))

    # Set frame with saving current frame as last
    def frame_set(self, frame: int, b_save: bool = True):
        if b_save:
            self.frame_last = self.scene.frame_current
        print("set frame to ", frame)
        self.scene.frame_set(frame)

    # Back to last frame
    def frame_set_last(self):
        if self.frame_last > 0:
            self.frame_set(self.frame_last)

    # Register tracker empty scene object
    def register_tracker(self, s_tracker_name: str) -> FTracker:
        tracker = FTracker(self.scene.objects[s_tracker_name])
        self.trackers[s_tracker_name] = tracker
        return tracker

    def get_or_register_tracker(self, s_tracker_name: str) -> FTracker:
        if s_tracker_name in self.trackers:
            return self.trackers[s_tracker_name]
        return self.register_tracker(s_tracker_name)

    # Get registered tracker
    def get_tracker(self, s_tracker_name: str) -> FTracker:
        return self.trackers[s_tracker_name]
