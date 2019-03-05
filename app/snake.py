class Snake(object):
    """
    Create a condensed snake object\n
    @param snake -> data to create snake object
    """

    def __init__(self, snake):
        self.id = snake['id']
        self.coords = self.body(snake)
        self.head = self.coords[0]
        self.tail = self.coords[-1]
        self.health = snake['health']
        self.length = len(self.coords)
        

    def body(self,snake):
        """
        Set snake body as 2d array vs array of objects\n
        @returns -> snake body
        """
        coords = []
        for i in snake['body']:
          coords.append([i['x'], i['y']])
        return coords
