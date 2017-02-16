from .modules import *

def init_Right_click_menu(self):
    #qpainterWindow Right-click menu
    self.qpainterWindow.setContextMenuPolicy(Qt.CustomContextMenu)
    self.qpainterWindow.customContextMenuRequested.connect(self.on_painter_context_menu)
    self.popMenu_painter = QMenu(self)
    self.action_painter_right_click_menu_add = QAction("Add a Point", self)
    self.popMenu_painter.addAction(self.action_painter_right_click_menu_add)
    self.action_painter_right_click_menu_fix_add = QAction("Add a Fixed Point", self)
    self.popMenu_painter.addAction(self.action_painter_right_click_menu_fix_add)
    self.action_painter_right_click_menu_path_add = QAction("Add a Path Point [Path Solving]", self)
    self.popMenu_painter.addAction(self.action_painter_right_click_menu_path_add)
    self.popMenu_painter.addSeparator()
    self.action_painter_right_click_menu_dimension_add = QAction("Show Dimension", self)
    self.popMenu_painter.addAction(self.action_painter_right_click_menu_dimension_add)
    self.action_painter_right_click_menu_dimension_path_track = QAction("Show Path Track", self)
    self.popMenu_painter.addAction(self.action_painter_right_click_menu_dimension_path_track)
    self.qpainterWindow.mouse_track.connect(self.context_menu_mouse_pos)
    #Entiteis_Point Right-click menu
    self.Entiteis_Point_Widget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.Entiteis_Point_Widget.customContextMenuRequested.connect(self.on_point_context_menu)
    self.popMenu_point = QMenu(self)
    self.action_point_right_click_menu_copy = QAction("Copy Coordinate", self)
    self.popMenu_point.addAction(self.action_point_right_click_menu_copy)
    self.action_point_right_click_menu_copyPoint = QAction("Copy Point", self)
    self.popMenu_point.addAction(self.action_point_right_click_menu_copyPoint)
    self.action_point_right_click_menu_add = QAction("Add a Point", self)
    self.popMenu_point.addAction(self.action_point_right_click_menu_add)
    self.action_point_right_click_menu_edit = QAction("Edit this Point", self)
    self.popMenu_point.addAction(self.action_point_right_click_menu_edit)
    self.action_point_right_click_menu_replace = QAction("Replace this Point", self)
    self.popMenu_point.addAction(self.action_point_right_click_menu_replace)
    self.action_point_right_click_menu_coverage = QAction("Coverage Coordinate", self)
    self.popMenu_point.addAction(self.action_point_right_click_menu_coverage)
    self.popMenu_point.addSeparator()
    self.action_point_right_click_menu_delete = QAction("Delete this Point", self)
    self.popMenu_point.addAction(self.action_point_right_click_menu_delete) 
    #Entiteis_Link Right-click menu
    self.Entiteis_Link_Widget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.Entiteis_Link_Widget.customContextMenuRequested.connect(self.on_link_context_menu)
    self.popMenu_link = QMenu(self)
    self.action_link_right_click_menu_add = QAction("Add a Link", self)
    self.popMenu_link.addAction(self.action_link_right_click_menu_add)
    self.action_link_right_click_menu_edit = QAction("Edit this Link", self)
    self.popMenu_link.addAction(self.action_link_right_click_menu_edit)
    self.action_link_right_click_menu_shaft = QAction("Turn this Link to Shaft", self)
    self.popMenu_link.addAction(self.action_link_right_click_menu_shaft)
    self.action_link_right_click_menu_reversion = QAction("Reverse Node point Y Coordinate", self)
    self.popMenu_link.addAction(self.action_link_right_click_menu_reversion)
    self.popMenu_link.addSeparator()
    self.action_link_right_click_menu_delete = QAction("Delete this Link", self)
    self.popMenu_link.addAction(self.action_link_right_click_menu_delete) 
    #Entiteis_Chain Right-click menu
    self.Entiteis_Stay_Chain_Widget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.Entiteis_Stay_Chain_Widget.customContextMenuRequested.connect(self.on_chain_context_menu)
    self.popMenu_chain = QMenu(self)
    self.action_chain_right_click_menu_add = QAction("Add a Chain", self)
    self.popMenu_chain.addAction(self.action_chain_right_click_menu_add)
    self.action_chain_right_click_menu_edit = QAction("Edit this Chain", self)
    self.popMenu_chain.addAction(self.action_chain_right_click_menu_edit)
    self.popMenu_chain.addSeparator()
    self.action_chain_right_click_menu_delete = QAction("Delete this Chain", self)
    self.popMenu_chain.addAction(self.action_chain_right_click_menu_delete) 
    #Drive_Shaft Right-click menu
    self.Drive_Shaft_Widget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.Drive_Shaft_Widget.customContextMenuRequested.connect(self.on_shaft_context_menu)
    self.popMenu_shaft = QMenu(self)
    self.action_shaft_right_click_menu_add = QAction("Add a Drive Shaft", self)
    self.popMenu_shaft.addAction(self.action_shaft_right_click_menu_add)
    self.action_shaft_right_click_menu_edit = QAction("Edit this Drive Shaft", self)
    self.popMenu_shaft.addAction(self.action_shaft_right_click_menu_edit)
    self.popMenu_shaft.addSeparator()
    self.action_shaft_right_click_menu_move_up = QAction("Move up", self)
    self.popMenu_shaft.addAction(self.action_shaft_right_click_menu_move_up)
    self.action_shaft_right_click_menu_move_down = QAction("Move down", self)
    self.popMenu_shaft.addAction(self.action_shaft_right_click_menu_move_down)
    self.popMenu_shaft.addSeparator()
    self.action_shaft_right_click_menu_delete = QAction("Delete this Drive Shaft", self)
    self.popMenu_shaft.addAction(self.action_shaft_right_click_menu_delete) 
    #Slider Right-click menu
    self.Slider_Widget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.Slider_Widget.customContextMenuRequested.connect(self.on_slider_context_menu)
    self.popMenu_slider = QMenu(self)
    self.action_slider_right_click_menu_add = QAction("Add a Slider", self)
    self.popMenu_slider.addAction(self.action_slider_right_click_menu_add)
    self.action_slider_right_click_menu_edit = QAction("Edit this Slider", self)
    self.popMenu_slider.addAction(self.action_slider_right_click_menu_edit)
    self.popMenu_slider.addSeparator()
    self.action_slider_right_click_menu_delete = QAction("Delete this Slider", self)
    self.popMenu_slider.addAction(self.action_slider_right_click_menu_delete) 
    #Rod Right-click menu
    self.Rod_Widget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.Rod_Widget.customContextMenuRequested.connect(self.on_rod_context_menu)
    self.popMenu_rod = QMenu(self)
    self.action_rod_right_click_menu_add = QAction("Add a Rod", self)
    self.popMenu_rod.addAction(self.action_rod_right_click_menu_add)
    self.action_rod_right_click_menu_edit = QAction("Edit this Rod", self)
    self.popMenu_rod.addAction(self.action_rod_right_click_menu_edit)
    self.popMenu_rod.addSeparator()
    self.action_rod_right_click_menu_delete = QAction("Delete this Rod", self)
    self.popMenu_rod.addAction(self.action_rod_right_click_menu_delete)
    #Parameter Right-click menu
    self.Parameter_Widget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.Parameter_Widget.customContextMenuRequested.connect(self.on_parameter_context_menu)
    self.popMenu_parameter = QMenu(self)
    self.action_parameter_right_click_menu_copy = QAction("Copy Parameter", self)
    self.popMenu_parameter.addAction(self.action_parameter_right_click_menu_copy)
    self.action_parameter_right_click_menu_add = QAction("Add a Parameter", self)
    self.popMenu_parameter.addAction(self.action_parameter_right_click_menu_add)
    self.popMenu_parameter.addSeparator()
    self.action_parameter_right_click_menu_move_up = QAction("Move up", self)
    self.popMenu_parameter.addAction(self.action_parameter_right_click_menu_move_up)
    self.action_parameter_right_click_menu_move_down = QAction("Move down", self)
    self.popMenu_parameter.addAction(self.action_parameter_right_click_menu_move_down)
    self.popMenu_parameter.addSeparator()
    self.action_parameter_right_click_menu_delete = QAction("Delete this Parameter", self)
    self.popMenu_parameter.addAction(self.action_parameter_right_click_menu_delete)

def actionEnabled(self):
    TWO_POINT = len(self.File.Lists.PointList)>1
    THREE_POINT = len(self.File.Lists.PointList)>2
    #Warning
    self.reqLine.setVisible(not TWO_POINT)
    self.reqChain.setVisible(not THREE_POINT)
    self.reqShaft.setVisible(not TWO_POINT)
    self.reqSlider.setVisible(not THREE_POINT)
    self.reqRod.setVisible(not THREE_POINT)
    self.reqPath.setVisible(not self.Drive_Shaft.rowCount()>0)
    self.reqPathSolving.setVisible(not self.File.PathSolvingReqs.list)
    #Add
    self.action_New_Line.setEnabled(TWO_POINT)
    self.action_New_Stay_Chain.setEnabled(THREE_POINT)
    self.action_Set_Drive_Shaft.setEnabled(TWO_POINT)
    self.action_Set_Slider.setEnabled(THREE_POINT)
    self.action_Set_Rod.setEnabled(THREE_POINT)
    self.action_link_right_click_menu_add.setEnabled(TWO_POINT)
    self.action_chain_right_click_menu_add.setEnabled(THREE_POINT)
    self.action_shaft_right_click_menu_add.setEnabled(TWO_POINT)
    self.action_slider_right_click_menu_add.setEnabled(THREE_POINT)
    self.action_rod_right_click_menu_add.setEnabled(THREE_POINT)
    #Edit
    self.actionEdit_Point.setEnabled(self.Entiteis_Point.rowCount()>1)
    self.actionEdit_Linkage.setEnabled(self.Entiteis_Link.rowCount()>0)
    self.actionEdit_Stay_Chain.setEnabled(self.Entiteis_Stay_Chain.rowCount()>0)
    self.action_Edit_Drive_Shaft.setEnabled(self.Drive_Shaft.rowCount()>0)
    self.action_Edit_Slider.setEnabled(self.Slider.rowCount()>0)
    self.action_Edit_Rod.setEnabled(self.Rod.rowCount()>0)
    self.action_link_right_click_menu_edit.setEnabled(self.Entiteis_Link.rowCount()>0)
    self.action_chain_right_click_menu_edit.setEnabled(self.Entiteis_Stay_Chain.rowCount()>0)
    self.action_shaft_right_click_menu_edit.setEnabled(self.Drive_Shaft.rowCount()>0)
    self.action_slider_right_click_menu_edit.setEnabled(self.Slider.rowCount()>0)
    self.action_rod_right_click_menu_edit.setEnabled(self.Rod.rowCount()>=1)
    #Delete
    self.actionDelete_Point.setEnabled(self.Entiteis_Point.rowCount()>1)
    self.actionDelete_Linkage.setEnabled(self.Entiteis_Link.rowCount()>0)
    self.actionDelete_Stay_Chain.setEnabled(self.Entiteis_Stay_Chain.rowCount()>0)
    self.actionDelete_Drive_Shaft.setEnabled(self.Drive_Shaft.rowCount()>0)
    self.actionDelete_Slider.setEnabled(self.Slider.rowCount()>0)
    self.actionDelete_Piston_Spring.setEnabled(self.Rod.rowCount()>0)
    self.action_link_right_click_menu_delete.setEnabled(self.Entiteis_Link.rowCount()>0)
    self.action_chain_right_click_menu_delete.setEnabled(self.Entiteis_Stay_Chain.rowCount()>0)
    self.action_shaft_right_click_menu_delete.setEnabled(self.Drive_Shaft.rowCount()>0)
    self.action_slider_right_click_menu_delete.setEnabled(self.Slider.rowCount()>0)
    self.action_rod_right_click_menu_delete.setEnabled(self.Rod.rowCount()>=1)
    #Panel
    self.PathTrack.setEnabled(self.Drive_Shaft.rowCount()>0)
    self.Measurement.setEnabled(self.Entiteis_Point.rowCount()>1)
    self.AuxLine.setEnabled(self.Entiteis_Point.rowCount()>1)
    self.Drive.setEnabled(self.Drive_Shaft.rowCount()>0)
    self.Drive_rod.setEnabled(self.Rod.rowCount()>0)
    #Others
    self.action_point_right_click_menu_copy.setVisible(self.Entiteis_Point.currentColumn()==4)
    self.action_link_right_click_menu_shaft.setEnabled(self.Entiteis_Link.rowCount()>0)
    self.action_link_right_click_menu_reversion.setEnabled(self.Entiteis_Link.rowCount()>0)
    self.action_Output_to_Solvespace.setEnabled(self.Entiteis_Link.rowCount()>0 or self.Entiteis_Stay_Chain.rowCount()>0)
    self.actionReplace_Point.setEnabled(TWO_POINT)
    self.action_point_right_click_menu_replace.setEnabled(TWO_POINT)
    self.actionBatch_moving.setEnabled(TWO_POINT)
    self.actionUndo.setEnabled(self.FileState.canUndo())
    self.actionRedo.setEnabled(self.FileState.canRedo())
