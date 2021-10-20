# This is a small program fot showing heliostat field
import matplotlib.pyplot as plt
import numpy as np


class Receiver:
    # type,pos,size,norm,face
    def __init__(self, id, t, p, s, n, f):
        # type,1 rectangle; 2,cylindrical
        self.id = int(id)
        self.type = int(t)
        self.pos = [float(i) for i in p]
        self.size = [float(i) for i in s]
        self.norm = [float(i) for i in n]
        self.face = int(f)

    def debug(self):
        print('id:', self.id)
        print('type:', self.type)
        print('pos:', self.pos)
        print('size:', self.size)
        print('norm:', self.norm)
        print('face:', self.face)
        pass


class Heliostat:
    def __init__(self, p, s):
        self.pos = [float(i) for i in p]
        self.size = [float(i) for i in s]

    def debug(self):
        print('pos:', self.pos)
        print('size:', self.size)


class Scene():
    def __init__(self):
        self.heliostats = []
        self.receiver = []

    def loadSceneFile(self, input_file_path):
        with open(input_file_path, 'r') as input_file:
            text = input_file.readline()
            while text:
                if text[0:5] == 'helio':
                    pos = self.__getPara(text, 'helio')
                    text = input_file.readline()
                    size = self.__getPara(text)
                    self.heliostats.append(Heliostat(pos, size))
                elif text[0:4] == 'Recv':

                    # type,pos,size,norm,face
                    type = self.__getPara(text, 'Recv')[0]
                    pos = None
                    size = None
                    norm = None
                    face = None
                    text = input_file.readline()
                    while (text and text[0:3] != 'end'):
                        if text[0:3] == 'pos':
                            pos = self.__getPara(text, 'pos')
                        elif text[0:4] == 'size':
                            size = self.__getPara(text, 'size')
                        elif text[0:4] == 'norm':
                            norm = self.__getPara(text, 'norm')
                        elif text[0:4] == 'face':
                            face = self.__getPara(text, 'face')[0]
                        else:
                            pass
                        text = input_file.readline()
                    rec = Receiver(len(self.receiver), type, pos, size, norm, face)
                    self.receiver.append(rec)
                elif text[0:1] == '#':
                    pass
                else:
                    pass
                text = input_file.readline()
        pass

    def debug(self):
        print("Receivers:")
        for i in self.receiver:
            i.debug()
        print("Heliostats:")
        for i in self.heliostats:
            i.debug()

    def showHeliostat(self):
        x = []
        y = []
        for i in self.heliostats:
            x.append(i.pos[0])
            y.append(i.pos[2])
        plt.scatter(x, y, marker='.', linewidths=0.01)
        plt.show()

    def exportHelioCSV(self, export_file_path="./export_scene.csv"):
        with open(export_file_path, 'w') as export_file:
            export_file.write('index, pos_x, pos_y, pos_z, size_x, size_y, size_z\n')
            for i, h in enumerate(self.heliostats):
                export_file.write(str(i))
                export_file.write(',')
                export_file.write(str(h.pos[0]))
                export_file.write(',')
                export_file.write(str(h.pos[1]))
                export_file.write(',')
                export_file.write(str(h.pos[2]))
                export_file.write(',')
                export_file.write(str(h.size[0]))
                export_file.write(',')
                export_file.write(str(h.size[1]))
                export_file.write(',')
                export_file.write(str(h.size[2]))
                export_file.write('\n')

    def __getPara(self, text, exclude=''):
        text = text.replace(' ', '\t')
        text = text.replace('\n', '\t')
        ret = text.split('\t')
        ret.remove(exclude)
        while '' in ret:
            ret.remove('')
        return ret


class MyClass:
    def __init__(self):
        self.a = 0

    def debug(self):
        print(self.a)


def showHeliostat():
    pass


if __name__ == "__main__":
    scene = Scene()
    scene.loadSceneFile('./Input/6282_QMCRT.scn')
    # scene.debug()
    scene.showHeliostat()
    # scene.exportHelioCSV("./text.csv")
