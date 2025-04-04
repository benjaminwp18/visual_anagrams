from .view_base import BaseView

class ViewChain(BaseView):
    def __init__(self, views: list[BaseView]):
        self.views = views

    def view(self, im):
        for view in self.views:
            im = view.view(im)
        return im

    def inverse_view(self, noise):
        for view in self.views:
            noise = view.inverse_view(noise)
        return noise

    def make_frame(self, im, t):
        # TODO: placeholder b/c we don't care about images
        return im