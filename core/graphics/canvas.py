# -*- coding: utf-8 -*-
##Pyslvs - Open Source Planar Linkage Mechanism Simulation and Dimensional Synthesis System.
##Copyright (C) 2016-2017 Yuan Chang
##E-mail: pyslvs@gmail.com
##
##This program is free software; you can redistribute it and/or modify
##it under the terms of the GNU Affero General Public License as published by
##the Free Software Foundation; either version 3 of the License, or
##(at your option) any later version.
##
##This program is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Affero General Public License for more details.
##
##You should have received a copy of the GNU Affero General Public License
##along with this program; if not, write to the Free Software
##Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from ..QtModules import *
from math import sqrt
from ..graphics.color import colorlist, colorName
tr = QCoreApplication.translate

class PointOptions:
    def __init__(self, width, height):
        self.ox = width/2
        self.oy = height/2
        self.rate = 2
        self.Path = Path()
        self.slvsPath = {'path':list(), 'show':False}
        self.currentShaft = 0

class Path:
    def __init__(self):
        self.path = list()
        self.demo = 0.
        self.show = True
        self.mode = True
        self.drive_mode = False
        defult_range = QRectF(QPointF(-50., 50.), QSizeF(100., 100.))
        self.ranges = [defult_range, defult_range]

class Selector:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.MiddleButtonDrag = False
    
    def distance(self, x, y):
        return round(sqrt((self.x-x)**2+(self.y-y)**2), 2)

class AuxLine:
    def __init__(self):
        self.show = False
        self.pt = 0
        self.horizontal = True
        self.vertical = True
        self.isMax = True
        self.isMin = True
        self.color = 6
        self.limit_color = 8
        self.maxX = 0
        self.maxY = 0
        self.minX = 0
        self.minY = 0

class BaseCanvas(QWidget):
    def __init__(self, parent=None):
        super(BaseCanvas, self).__init__(parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.options = PointOptions(self.width(), self.height())
        self.AuxLine = AuxLine()
        self.linkWidth = 3
        self.pathWidth = 3
        self.Color = colorlist()
        self.Font_size = 10
        self.Point_mark = True
        self.showDimension = True
    
    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.fillRect(event.rect(), QBrush(Qt.white))
    
    def drawPoint(self, i, x, y, fix, color, cx, cy):
        pen = QPen()
        pen.setWidth(2)
        pen.setColor(color)
        self.painter.setPen(pen)
        if fix:
            self.painter.drawPolygon(QPointF(x, y), QPointF(x-10, y+20), QPointF(x+10, y+20))
            self.painter.drawEllipse(QPointF(x, y), 10., 10.)
        else:
            self.painter.drawEllipse(QPointF(x, y), 5., 5.)
        if self.Point_mark:
            pen.setColor(Qt.darkGray)
            pen.setWidth(2)
            self.painter.setPen(pen)
            self.painter.setFont(QFont('Arial', self.Font_size))
            text = '[{}]'.format(i) if type(i)==str else '[Point{}]'.format(i)
            if self.showDimension:
                text += ':({:.02f}, {:.02f})'.format(cx, cy)
            self.painter.drawText(QPointF(x+6, y-6), text)
    
    def drawLink(self, i, x0, y0, x1, y1, length):
        pen = QPen()
        pen.setWidth(self.linkWidth)
        pen.setColor(Qt.darkGray)
        self.painter.setPen(pen)
        self.painter.drawLine(QPointF(x0, y0), QPointF(x1, y1))
        if self.Point_mark:
            pen.setColor(Qt.darkGray)
            self.painter.setPen(pen)
            self.painter.setFont(QFont('Arial', self.Font_size))
            text = '[{}]'.format(i) if type(i)==str else '[Line{}]'.format(i)
            if self.showDimension:
                text += ':{:.02f}'.format(length)
            self.painter.drawText(QPointF((x0+x1)/2, (y0+y1)/2), text)
    
    def drawChain(self, i, x0, y0, x1, y1, x2, y2, p1p2, p2p3, p1p3):
        pen = QPen()
        pen.setWidth(self.linkWidth)
        pen.setColor(Qt.darkGray)
        self.painter.setPen(pen)
        self.painter.setBrush(QColor(226, 219, 190))
        self.painter.drawPolygon(QPointF(x0, y0), QPointF(x1, y1), QPointF(x2, y2))
        self.painter.setBrush(Qt.NoBrush)
        if self.Point_mark:
            pen.setColor(Qt.darkGray)
            self.painter.setPen(pen)
            self.painter.setFont(QFont('Arial', self.Font_size))
            text = '[Chain{}]'.format(i)
            if self.showDimension:
                self.painter.drawText(QPointF((x0+x1)/2, (y0+y1)/2), text+':{:.02f}'.format(p1p2))
                self.painter.drawText(QPointF((x1+x2)/2, (y1+y2)/2), text+':{:.02f}'.format(p2p3))
                self.painter.drawText(QPointF((x0+x2)/2, (y0+y2)/2), text+':{:.02f}'.format(p1p3))
            else:
                self.painter.drawText(QPointF((x0+x1+x2)/3, (y0+y1+y2)/3), text)
    
    def drawShaft(self, i, x0, y0, x1, y1):
        pen = QPen()
        pen.setWidth(self.linkWidth+2)
        pen.setColor(QColor(225, 140, 0) if i==self.options.currentShaft else QColor(175, 90, 0))
        self.painter.setPen(pen)
        self.painter.drawLine(QPointF(x0, y0), QPointF(x1, y1))

class DynamicCanvas(BaseCanvas):
    mouse_track = pyqtSignal(float, float)
    mouse_getSelection = pyqtSignal(list)
    mouse_noSelection = pyqtSignal()
    mouse_getDoubleClickAdd = pyqtSignal()
    mouse_getDoubleClickEdit = pyqtSignal(int)
    change_event = pyqtSignal()
    zoom_change = pyqtSignal(int)
    def __init__(self, parent=None):
        super(DynamicCanvas, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStatusTip(tr("DynamicCanvas", "Use mouse wheel or middle button to look around."))
        self.rotateAngle = 0
        self.Selector = Selector()
        self.reset_Auxline()
        self.re_Color = colorName()
        self.pointsSelection = list()
        self.zoom = 2*self.options.rate
        self.linkWidth = 3
        self.pathWidth = 3
        self.rotateAngle = 0.
        self.showDimension = False
    
    def update_figure(self, Point, Line, Chain, Shaft, Slider, Rod, path):
        self.Point = Point
        self.Line = Line
        self.Chain = Chain
        self.Shaft = Shaft
        self.Slider = Slider
        self.Rod = Rod
        self.options.Path.path = path
        self.update()
    
    @pyqtSlot(int)
    def setLinkWidth(self, linkWidth):
        self.linkWidth = linkWidth
        self.update()
    
    @pyqtSlot(int)
    def setPathWidth(self, pathWidth):
        self.pathWidth = pathWidth
        self.update()
    
    @pyqtSlot(float)
    def setRotateAngle(self, rotateAngle):
        self.rotateAngle = rotateAngle
        self.update()
    
    @pyqtSlot(bool)
    def setPointMark(self, PointMark):
        self.Point_mark = PointMark
        self.update()
    
    @pyqtSlot(bool)
    def setShowDimension(self, showDimension):
        self.showDimension = showDimension
        self.update()
    
    @pyqtSlot(int)
    def setFontSize(self, fontSize):
        self.Font_size = fontSize
        self.update()
    
    @pyqtSlot(int)
    def setZoom(self, zoom):
        self.zoom = zoom/100*self.options.rate
        self.update()
    
    def changePointsSelection(self, pointsSelection):
        self.pointsSelection = pointsSelection
        self.update()
    
    def changePathCurrentShaft(self):
        if self.Shaft:
            self.options.Path.demo = self.Shaft[self.options.currentShaft].demo
    
    @pyqtSlot(int)
    def changeCurrentShaft(self, pos=0):
        self.options.currentShaft = pos
        self.update()
    
    def path_solving(self, path=list()):
        self.options.slvsPath['path'] = path
        self.update()
    
    @pyqtSlot(tuple, float, tuple, float)
    def update_ranges(self, point1, range1, point2, range2):
        self.options.Path.ranges[0] = QRectF(QPointF(point1[0]-range1/2, point1[1]+range1/2), QSizeF(range1, range1))
        self.options.Path.ranges[1] = QRectF(QPointF(point2[0]-range2/2, point2[1]+range2/2), QSizeF(range2, range2))
        self.update()
    
    def paintEvent(self, event):
        super(DynamicCanvas, self).paintEvent(event)
        self.painter.translate(self.options.ox, self.options.oy)
        self.painter.rotate(self.rotateAngle)
        pathShaft = None
        if self.options.Path.drive_mode:
            for vpaths in self.options.Path.path:
                if vpaths.shaft==self.options.currentShaft:
                    pathShaft = vpaths
        if (not pathShaft==None) and (not pathShaft.isBroken()):
            shaft = self.Shaft[pathShaft.shaft]
            resolution = abs(shaft.end-shaft.start)/(len(pathShaft.paths[0].path)-1)
            resolutionIndex = int(round(self.options.Path.demo/resolution))
            Points = {e.point:e for e in pathShaft.paths}
            for i, e in enumerate(self.Chain):
                p1x = (self.Point[e.p1].cx if self.Point[e.p1].fix else Points[e.p1].path[resolutionIndex][0])*self.zoom
                p1y = (self.Point[e.p1].cy if self.Point[e.p1].fix else Points[e.p1].path[resolutionIndex][1])*self.zoom*-1
                p2x = (self.Point[e.p2].cx if self.Point[e.p2].fix else Points[e.p2].path[resolutionIndex][0])*self.zoom
                p2y = (self.Point[e.p2].cy if self.Point[e.p2].fix else Points[e.p2].path[resolutionIndex][1])*self.zoom*-1
                p3x = (self.Point[e.p3].cx if self.Point[e.p3].fix else Points[e.p3].path[resolutionIndex][0])*self.zoom
                p3y = (self.Point[e.p3].cy if self.Point[e.p3].fix else Points[e.p3].path[resolutionIndex][1])*self.zoom*-1
                self.drawChain(i, p1x, p1y, p2x, p2y, p3x, p3y, e.p1p2, e.p2p3, e.p1p3)
            for i, e in enumerate(self.Line):
                p1x = (self.Point[e.start].cx if self.Point[e.start].fix else Points[e.start].path[resolutionIndex][0])*self.zoom
                p1y = (self.Point[e.start].cy if self.Point[e.start].fix else Points[e.start].path[resolutionIndex][1])*self.zoom*-1
                p2x = (self.Point[e.end].cx if self.Point[e.end].fix else Points[e.end].path[resolutionIndex][0])*self.zoom
                p2y = (self.Point[e.end].cy if self.Point[e.end].fix else Points[e.end].path[resolutionIndex][1])*self.zoom*-1
                self.drawLink(i, p1x, p1y, p2x, p2y, e.len)
            for i, e in enumerate(self.Slider):
                p1x = (self.Point[e.start].cx if self.Point[e.start].fix else Points[e.start].path[resolutionIndex][0])*self.zoom
                p1y = (self.Point[e.start].cy if self.Point[e.start].fix else Points[e.start].path[resolutionIndex][1])*self.zoom*-1
                p2x = (self.Point[e.end].cx if self.Point[e.end].fix else Points[e.end].path[resolutionIndex][0])*self.zoom
                p2y = (self.Point[e.end].cy if self.Point[e.end].fix else Points[e.end].path[resolutionIndex][1])*self.zoom*-1
                self.drawSlider(i, p1x, p1y, p2x, p2y, p3x, p3y)
            for i, e in enumerate(self.Rod):
                p1x = (self.Point[e.start].cx if self.Point[e.start].fix else Points[e.start].path[resolutionIndex][0])*self.zoom
                p1y = (self.Point[e.start].cy if self.Point[e.start].fix else Points[e.start].path[resolutionIndex][1])*self.zoom*-1
                p2x = (self.Point[e.end].cx if self.Point[e.end].fix else Points[e.end].path[resolutionIndex][0])*self.zoom
                p2y = (self.Point[e.end].cy if self.Point[e.end].fix else Points[e.end].path[resolutionIndex][1])*self.zoom*-1
                p3x = (self.Point[e.cen].cx if self.Point[e.cen].fix else Points[e.cen].path[resolutionIndex][0])*self.zoom
                p3y = (self.Point[e.cen].cy if self.Point[e.cen].fix else Points[e.cen].path[resolutionIndex][1])*self.zoom*-1
                self.drawRod(i, p1x, p1y, p2x, p2y, p3x, p3y, e.pos)
            for i, e in enumerate(self.Shaft):
                p1x = (self.Point[e.cen].cx if self.Point[e.cen].fix else Points[e.cen].path[resolutionIndex][0])*self.zoom
                p1y = (self.Point[e.cen].cy if self.Point[e.cen].fix else Points[e.cen].path[resolutionIndex][1])*self.zoom*-1
                p2x = (self.Point[e.ref].cx if self.Point[e.ref].fix else Points[e.ref].path[resolutionIndex][0])*self.zoom
                p2y = (self.Point[e.ref].cy if self.Point[e.ref].fix else Points[e.ref].path[resolutionIndex][1])*self.zoom*-1
                self.drawShaft(i, p1x, p1y, p2x, p2y)
            if self.AuxLine.show:
                self.drawAuxLine(
                    self.Point[self.AuxLine.pt].cx if self.Point[self.AuxLine.pt].fix else Points[self.AuxLine.pt].path[resolutionIndex][0],
                    self.Point[self.AuxLine.pt].cy if self.Point[self.AuxLine.pt].fix else Points[self.AuxLine.pt].path[resolutionIndex][1])
            self.drawPath()
            for path in pathShaft.paths:
                x = path.path[resolutionIndex][0]*self.zoom
                y = path.path[resolutionIndex][1]*self.zoom*-1
                self.drawPoint(path.point, x, y, self.Point[path.point].fix, self.Color[self.Point[path.point].color], x/self.zoom, y/self.zoom*-1)
            for i, e in enumerate(self.Point):
                if i in Points:
                    continue
                x = e.cx*self.zoom
                y = e.cy*self.zoom*-1
                self.drawPoint(i, x, y, e.fix, self.Color[e.color], e.cx, e.cy)
        else:
            for i, e in enumerate(self.Chain):
                p1x = self.Point[e.p1].cx*self.zoom
                p1y = self.Point[e.p1].cy*self.zoom*-1
                p2x = self.Point[e.p2].cx*self.zoom
                p2y = self.Point[e.p2].cy*self.zoom*-1
                p3x = self.Point[e.p3].cx*self.zoom
                p3y = self.Point[e.p3].cy*self.zoom*-1
                self.drawChain(i, p1x, p1y, p2x, p2y, p3x, p3y, e.p1p2, e.p2p3, e.p1p3)
            for i, e in enumerate(self.Line):
                p1x = self.Point[e.start].cx*self.zoom
                p1y = self.Point[e.start].cy*self.zoom*-1
                p2x = self.Point[e.end].cx*self.zoom
                p2y = self.Point[e.end].cy*self.zoom*-1
                self.drawLink(i, p1x, p1y, p2x, p2y, e.len)
            for i, e in enumerate(self.Slider):
                p1x = self.Point[e.start].cx*self.zoom
                p1y = self.Point[e.start].cy*self.zoom*-1
                p2x = self.Point[e.end].cx*self.zoom
                p2y = self.Point[e.end].cy*self.zoom*-1
                p3x = self.Point[e.cen].cx*self.zoom
                p3y = self.Point[e.cen].cy*self.zoom*-1
                self.drawSlider(i, p1x, p1y, p2x, p2y, p3x, p3y)
            for i, e in enumerate(self.Rod):
                p1x = self.Point[e.start].cx*self.zoom
                p1y = self.Point[e.start].cy*self.zoom*-1
                p2x = self.Point[e.end].cx*self.zoom
                p2y = self.Point[e.end].cy*self.zoom*-1
                p3x = self.Point[e.cen].cx*self.zoom
                p3y = self.Point[e.cen].cy*self.zoom*-1
                self.drawRod(i, p1x, p1y, p2x, p2y, p3x, p3y, e.pos)
            for i, e in enumerate(self.Shaft):
                p1x = self.Point[e.cen].cx*self.zoom
                p1y = self.Point[e.cen].cy*self.zoom*-1
                p2x = self.Point[e.ref].cx*self.zoom
                p2y = self.Point[e.ref].cy*self.zoom*-1
                self.drawShaft(i, p1x, p1y, p2x, p2y)
            if self.AuxLine.show:
                self.drawAuxLine(self.Point[self.AuxLine.pt].cx, self.Point[self.AuxLine.pt].cy)
            self.drawPath()
            for i, e in enumerate(self.Point):
                x = e.cx*self.zoom
                y = e.cy*self.zoom*-1
                self.drawPoint(i, x, y, e.fix, self.Color[e.color], e.cx, e.cy)
        if self.options.slvsPath['path'] and self.options.slvsPath['show']:
            pen = QPen()
            pathData = self.options.slvsPath['path']
            pen.setWidth(self.pathWidth)
            pen.setColor(QColor(69, 247, 232))
            self.painter.setPen(pen)
            if self.options.Path.mode==True:
                if len(pathData)>1:
                    pointPath = QPainterPath()
                    for i, e in enumerate(pathData):
                        x = e['x']*self.zoom
                        y = e['y']*self.zoom*-1
                        if i==0:
                            pointPath.moveTo(x, y)
                        else:
                            pointPath.lineTo(QPointF(x, y))
                    self.painter.drawPath(pointPath)
                elif len(pathData)==1:
                    self.painter.drawPoint(QPointF(pathData[0]['x']*self.zoom, pathData[0]['y']*self.zoom*-1))
            else:
                for i, e in enumerate(pathData):
                    x = e['x']*self.zoom
                    y = e['y']*self.zoom*-1
                    self.painter.drawPoint(QPointF(x, y))
        self.painter.end()
        self.change_event.emit()
    
    def drawPoint(self, i, x, y, fix, color, cx=0, cy=0):
        super(DynamicCanvas, self).drawPoint(i, x, y, fix, color, cx, cy)
        if i in self.pointsSelection:
            pen = QPen()
            pen.setWidth(3)
            pen.setColor(QColor(161, 16, 239))
            self.painter.setPen(pen)
            self.painter.drawRect(x-12, y-12, 24, 24)
    
    def drawSlider(self, i, x0, y0, x1, y1, x2, y2):
        pen = QPen()
        pen.setWidth(self.linkWidth)
        pen.setColor(Qt.darkMagenta)
        self.painter.setPen(pen)
        self.painter.drawLine(QPointF(x0, y0), QPointF(x1, y1))
    
    def drawRod(self, i, x0, y0, x1, y1, x2, y2, pos):
        pen = QPen()
        pen.setWidth(self.linkWidth)
        pen.setColor(Qt.darkRed)
        self.painter.setPen(pen)
        self.painter.drawLine(QPointF(x0, y0), QPointF(x1, y1))
        if self.showDimension:
            pen.setColor(Qt.darkGray)
            self.painter.setPen(pen)
            self.painter.setFont(QFont('Arial', self.Font_size))
            self.painter.drawText(QPointF(x2+6, y2+6), '{{{}}}'.format(pos))
    
    def drawAuxLine(self, x, y):
        pen = QPen(Qt.DashDotLine)
        pen.setColor(self.Color[self.re_Color[self.AuxLine.limit_color]])
        pen.setWidth(self.linkWidth)
        self.painter.setPen(pen)
        if self.AuxLine.isMax:
            if self.AuxLine.maxX<x:
                self.AuxLine.maxX = x
            if self.AuxLine.maxY<y:
                self.AuxLine.maxY = y
        if self.AuxLine.isMin:
            if self.AuxLine.minX>x:
                self.AuxLine.minX = x
            if self.AuxLine.minY>y:
                self.AuxLine.minY = y
        for isl, lx, ly in zip(
                [self.AuxLine.isMax, self.AuxLine.isMin],
                [self.AuxLine.maxX, self.AuxLine.minX],
                [self.AuxLine.maxY, self.AuxLine.minY]):
            if isl:
                L_point = QPointF(self.width()*4, ly*self.zoom*-1)
                R_point = QPointF(self.width()*-4, ly*self.zoom*-1)
                U_point = QPointF(lx*self.zoom, self.height()*4)
                D_point = QPointF(lx*self.zoom, self.height()*-4)
                self.painter.drawLine(L_point, R_point)
                self.painter.drawLine(U_point, D_point)
                if self.showDimension:
                    text_center_x = QPointF(lx*self.zoom+self.linkWidth, self.options.oy*-1+self.Font_size)
                    text_center_y = QPointF(self.options.ox*-1, ly*self.zoom*-1-self.linkWidth)
                    self.painter.setFont(QFont('Arial', self.Font_size))
                    self.painter.drawText(text_center_x, '{:.6f}'.format(lx))
                    self.painter.drawText(text_center_y, '{:.6f}'.format(ly))
        pen.setColor(self.Color[self.re_Color[self.AuxLine.color]])
        L_point = QPointF(self.width()*4, y*self.zoom*-1)
        R_point = QPointF(self.width()*-4, y*self.zoom*-1)
        U_point = QPointF(x*self.zoom, self.height()*4)
        D_point = QPointF(x*self.zoom, self.height()*-4)
        self.painter.setPen(pen)
        if self.AuxLine.horizontal:
            self.painter.drawLine(L_point, R_point)
        if self.AuxLine.vertical:
            self.painter.drawLine(U_point, D_point)
    
    def drawPath(self):
        if self.options.Path.show:
            for vpaths in self.options.Path.path:
                for vpath in vpaths.paths:
                    if vpath.show:
                        pen = QPen()
                        pen.setWidth(self.pathWidth)
                        if vpaths.shaft==self.options.currentShaft:
                            pen.setColor(self.Color[self.Point[vpath.point].color])
                        else:
                            pen.setColor(self.Color['Gray'])
                        self.painter.setPen(pen)
                        if self.options.Path.mode==True:
                            error = False
                            pointPath = QPainterPath()
                            for i, point in enumerate(vpath.path):
                                if point is None or point[0] is None or point[0] is False:
                                    error = True
                                    continue
                                x = point[0]*self.zoom
                                y = point[1]*self.zoom*-1
                                if i==0 or error:
                                    pointPath.moveTo(x, y)
                                    error = False
                                else:
                                    pointPath.lineTo(QPointF(x, y))
                            self.painter.drawPath(pointPath)
                        else:
                            for i, point in enumerate(vpath.path):
                                if point[0] is None or point[0] is False:
                                    continue
                                x = point[0]*self.zoom
                                y = point[1]*self.zoom*-1
                                self.painter.drawPoint(QPointF(x, y))
        if self.options.slvsPath['show']:
            for (i, rect), range_color in zip(enumerate(self.options.Path.ranges), [QColor(138, 21, 196, 30), QColor(74, 178, 176, 30)]):
                pen = QPen()
                pen.setColor(range_color)
                self.painter.setBrush(range_color)
                self.painter.setPen(pen)
                cx = rect.x()*self.zoom
                cy = rect.y()*-self.zoom
                self.painter.drawRect(QRectF(cx, cy, rect.width()*self.zoom, rect.height()*self.zoom))
                range_color.setAlpha(100)
                pen.setColor(range_color)
                pen.setWidth(2)
                self.painter.setPen(pen)
                self.painter.setBrush(Qt.NoBrush)
                self.painter.drawRect(QRectF(cx, cy, rect.width()*self.zoom, rect.height()*self.zoom))
                self.painter.setFont(QFont('Arial', self.Font_size+5))
                range_color.setAlpha(255)
                pen.setColor(range_color)
                self.painter.setPen(pen)
                if i==0:
                    self.painter.drawText(QPointF(cx-70+rect.width()*self.zoom, cy-6), 'Driver')
                else:
                    self.painter.drawText(QPointF(cx+6, cy-6), 'Follower')
    
    def Reset_Aux_limit(self):
        self.AuxLine.maxX = self.Point[self.AuxLine.pt].cx
        self.AuxLine.maxY = self.Point[self.AuxLine.pt].cy
        self.AuxLine.minX = self.Point[self.AuxLine.pt].cx
        self.AuxLine.minY = self.Point[self.AuxLine.pt].cy
    
    def reset_Auxline(self):
        self.AuxLine = AuxLine()
    
    def mousePressEvent(self, event):
        self.Selector.x = event.x()-self.options.ox
        self.Selector.y = event.y()-self.options.oy
        if event.buttons()==Qt.LeftButton:
            selection = []
            for i, e in enumerate(self.Point):
                x = e.cx*self.zoom
                y = e.cy*self.zoom*-1
                if self.Selector.distance(x, y)<10:
                    selection.append(i)
            if selection:
                self.mouse_getSelection.emit(selection)
            else:
                self.mouse_noSelection.emit()
        if event.buttons()==Qt.MiddleButton:
            self.Selector.MiddleButtonDrag = True
    
    def mouseReleaseEvent(self, event):
        self.Selector.MiddleButtonDrag = False
    
    def mouseDoubleClickEvent(self, event):
        if event.button()==Qt.MidButton:
            self.SetIn()
        if event.buttons()==Qt.LeftButton:
            if QApplication.keyboardModifiers()==Qt.AltModifier:
                self.mouse_getDoubleClickAdd.emit()
            else:
                self.Selector.x = event.x()-self.options.ox
                self.Selector.y = event.y()-self.options.oy
                for i, e in enumerate(self.Point):
                    x = e.cx*self.zoom
                    y = e.cy*self.zoom*-1
                    if self.Selector.distance(x, y)<10:
                        self.mouse_getDoubleClickEdit.emit(i)
                        break
    
    def mouseMoveEvent(self, event):
        if self.Selector.MiddleButtonDrag:
            self.options.ox = event.x()-self.Selector.x
            self.options.oy = event.y()-self.Selector.y
            self.update()
        self.mouse_track.emit((event.x()-self.options.ox)/self.zoom, -((event.y()-self.options.oy)/self.zoom))
        if QApplication.keyboardModifiers()==Qt.AltModifier:
            self.setCursor(Qt.CrossCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
    
    def resizeEvent(self, event):
        self.SetIn()
    
    def SetIn(self):
        width = self.width()
        height = self.height()
        height = height if not height==0 else 1
        if len(self.Point)==1:
            self.zoom_change.emit(200)
            self.options.ox = width/2
            self.options.oy = height/2
        else:
            Xs = [e.cx for e in self.Point]
            Ys = [e.cy for e in self.Point]
            if self.options.Path.path:
                Path = self.options.Path.path
                pathMaxX = max([max([max([dot[0] for dot in vpath.path]) for vpath in vpaths.paths]) for vpaths in Path])
                pathMinX = min([min([min([dot[0] for dot in vpath.path]) for vpath in vpaths.paths]) for vpaths in Path])
                pathMaxY = max([max([max([dot[1] for dot in vpath.path]) for vpath in vpaths.paths]) for vpaths in Path])
                pathMinY = min([min([min([dot[1] for dot in vpath.path]) for vpath in vpaths.paths]) for vpaths in Path])
                diffX = max(max(Xs), pathMaxX)-min(min(Xs), pathMinX)
                diffY = max(max(Ys), pathMaxY)-min(min(Ys), pathMinY)
                cenx = (min(min(Xs), pathMinX)+max(max(Xs), pathMaxX))/2
                ceny = (min(min(Ys), pathMinY)+max(max(Ys), pathMaxY))/2
            else:
                diffX = max(Xs)-min(Xs)
                diffY = max(Ys)-min(Ys)
                cenx = (min(Xs)+max(Xs))/2
                ceny = (min(Ys)+max(Ys))/2
            cdiff = diffX/diffY > width/height
            self.zoom_change.emit(int((width if cdiff else height)/(diffX if cdiff else diffY)*0.95*50))
            self.options.ox = (width/2)-cenx*self.zoom
            self.options.oy = (height/2)+ceny*self.zoom
        self.update()