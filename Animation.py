import pygame


class Animation:
    def __init__(self, images, times):
        self.anim = []
        for (img, time) in zip(images, times):
            self.anim.append((img, time))
        self.time = 0
        self.times = times
        self.current_image = images[0]
    
    def update_anim(self):
        self.time += 1
        current_time = 0
        for frame in self.anim:
            current_time += frame[1]
            if current_time > self.time:
                self.current_image = frame[0]
                break
        if sum(self.times) < self.time:
            self.time = 0
        print(self.time)
