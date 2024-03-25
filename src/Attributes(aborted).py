class Attributes:
    def __init__(self, name, inRange, outRange, inRange_liked, outRange_liked):
        self.name = name
        self.inRange = inRange
        self.outRange = outRange
        self.inRange_liked = inRange_liked
        self.outRange_liked = outRange_liked
        self.inRange_disliked = inRange-inRange_liked  # Assuming initialization to 0 for high_disliked
        self.outRange_disliked = outRange-outRange_liked   # Assuming initialization to 0 for low_disliked

    def add_InRange(self, increase):
        self.inRange += increase

    def add_OutofRange(self, increase):
        self.outRange += increase

    def add_inRangeLiked(self, increase):
        self.inRange_liked += increase

    def add_outOfRangeLiked(self, increase):
        self.outRange_liked += increase

    def add_InRangedisliked(self, increase):
        self.inRange_disliked += increase

    def add_outOfRangedisliked(self, increase):
        self.outRange_disliked += increase

    def get_outOfRange(self):
        return self.outRange

    def get_inRange(self):
        return self.inRange

    def get_InRangeliked(self):
        return self.inRange_liked

    def get_inRangeDisliked(self):
        return self.inRange_disliked

    def get_outOfRangeLiked(self):
        return self.outRange_liked

    def get_outOfRangeDisliked(self):
        return self.outRange_disliked