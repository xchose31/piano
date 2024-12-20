import pygame
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow, QTableWidget, \
    QTableWidgetItem, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
from PyQt6 import uic
import sys
import sqlite3
import os
import io

class after_in_keys(Exception):
    pass

teamplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>596</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Создание уровня</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="continue_btn">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>350</y>
      <width>171</width>
      <height>71</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size:20px;</string>
    </property>
    <property name="text">
     <string>Подтвердить</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>30</y>
      <width>101</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Название уровня:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>80</y>
      <width>81</width>
      <height>61</height>
     </rect>
    </property>
    <property name="text">
     <string>Ноты:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="do_btn">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>140</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>До</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">notes_btns</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="re_btn">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>140</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Ре</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">notes_btns</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="mi_btn">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>140</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Ми</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">notes_btns</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="fa_btn">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>140</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Фа</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">notes_btns</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="so_btn">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>140</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Соль</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">notes_btns</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="la_btn">
    <property name="geometry">
     <rect>
      <x>480</x>
      <y>140</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Ля</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">notes_btns</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="si_btn">
    <property name="geometry">
     <rect>
      <x>570</x>
      <y>140</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Си</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">notes_btns</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="one_btn">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>180</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>1</string>
    </property>
   </widget>
   <widget class="QPushButton" name="two_btn">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>180</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>2</string>
    </property>
   </widget>
   <widget class="QPushButton" name="diez_btn">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>180</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Диез</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lvl_name">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>50</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QSpinBox" name="time_spin">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>270</y>
      <width>42</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QTextBrowser" name="textBrowser">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>260</y>
      <width>151</width>
      <height>192</height>
     </rect>
    </property>
    <property name="html">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Ограничение времени:&lt;br /&gt;(если вы не хотите добавлять ограничение по времени уровню, оставьте значение 0)&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="notes_text">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>100</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="clear_btn">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>100</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Очистить</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="notes_btns"/>
 </buttongroups>
</ui>
"""

teamplate2 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>mainWindow</class>
 <widget class="QMainWindow" name="mainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>910</width>
    <height>710</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="windowTitle">
   <string>Пианино</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="Do1">
    <property name="geometry">
     <rect>
      <x>94</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Do1{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Do1:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


Q</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Re1">
    <property name="geometry">
     <rect>
      <x>134</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Re1{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Re1:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


W</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Mi1">
    <property name="geometry">
     <rect>
      <x>174</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Mi1{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Mi1:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


E</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Fa1">
    <property name="geometry">
     <rect>
      <x>214</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Fa1{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Fa1:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


R</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Sol1">
    <property name="geometry">
     <rect>
      <x>254</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Sol1{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Sol1:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


T</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="La1">
    <property name="geometry">
     <rect>
      <x>294</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#La1{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#La1:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


Y</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Si1">
    <property name="geometry">
     <rect>
      <x>334</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Si1{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Si1:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


U</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Do2">
    <property name="geometry">
     <rect>
      <x>374</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Do2{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Do2:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


I</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Re2">
    <property name="geometry">
     <rect>
      <x>414</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Re2{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Re2:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


O</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Mi2">
    <property name="geometry">
     <rect>
      <x>454</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Mi2{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Mi2:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


P</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Fa2">
    <property name="geometry">
     <rect>
      <x>494</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Fa2{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Fa2:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


Z</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Sol2">
    <property name="geometry">
     <rect>
      <x>534</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Sol2{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Sol2:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


X</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="La2">
    <property name="geometry">
     <rect>
      <x>574</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#La2{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#La2:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


C</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Si2">
    <property name="geometry">
     <rect>
      <x>614</x>
      <y>390</y>
      <width>41</width>
      <height>181</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Si2{
background-color: rgb(242, 242, 242);
background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));
font-size: 25px;
color:Black;
}


#Si2:pressed{
background-color: rgb(250, 250, 250);

}</string>
    </property>
    <property name="text">
     <string>


V</string>
    </property>
    <property name="shortcut">
     <string>A</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Do1_diez">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>115</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="tabletTracking">
     <bool>false</bool>
    </property>
    <property name="acceptDrops">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">#Do1_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#Do1_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>2</string>
    </property>
    <property name="shortcut">
     <string>Q</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Re1_diez">
    <property name="geometry">
     <rect>
      <x>161</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Re1_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#Re1_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>3</string>
    </property>
    <property name="shortcut">
     <string>W</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="La1_diez">
    <property name="geometry">
     <rect>
      <x>322</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#La1_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#La1_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>7</string>
    </property>
    <property name="shortcut">
     <string>W</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Fa1_diez">
    <property name="geometry">
     <rect>
      <x>234</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Fa1_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#Fa1_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>5</string>
    </property>
    <property name="shortcut">
     <string>W</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Sol1_diez">
    <property name="geometry">
     <rect>
      <x>278</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Sol1_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#Sol1_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>6</string>
    </property>
    <property name="shortcut">
     <string>W</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Do2_diez">
    <property name="geometry">
     <rect>
      <x>394</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Do2_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#Do2_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>9</string>
    </property>
    <property name="shortcut">
     <string>W</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Re2_diez">
    <property name="geometry">
     <rect>
      <x>439</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Re2_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#Re2_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>0</string>
    </property>
    <property name="shortcut">
     <string>W</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Fa2_diez">
    <property name="geometry">
     <rect>
      <x>514</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Fa2_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#Fa2_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>S</string>
    </property>
    <property name="shortcut">
     <string>W</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="Sol2_diez">
    <property name="geometry">
     <rect>
      <x>557</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#Sol2_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#Sol2_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>D</string>
    </property>
    <property name="shortcut">
     <string>W</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="La2_diez">
    <property name="geometry">
     <rect>
      <x>600</x>
      <y>390</y>
      <width>31</width>
      <height>111</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">#La2_diez{
background-color: rgb(0, 0, 0);
background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));
color: White;
font-size: 22px;
}
#La2_diez:pressed{
background-color: rgb(0, 0, 0);

	background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));

}
</string>
    </property>
    <property name="text">
     <string>F</string>
    </property>
    <property name="shortcut">
     <string>W</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Notes_keys</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="change_btn">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>40</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Изменить клавишу</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="key_before">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="key_after">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>40</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>40</y>
      <width>31</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size:20px;</string>
    </property>
    <property name="text">
     <string>-&gt;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="add_lvl_btn">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>90</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Создать уровень</string>
    </property>
   </widget>
   <widget class="QPushButton" name="start_lvl_btn">
    <property name="geometry">
     <rect>
      <x>639</x>
      <y>100</y>
      <width>121</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Начать уровень</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>610</x>
      <y>40</y>
      <width>241</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Выбрать уровень:(номер или название)</string>
    </property>
   </widget>
   <widget class="QPushButton" name="stop_btn">
    <property name="geometry">
     <rect>
      <x>640</x>
      <y>170</y>
      <width>121</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Стоп</string>
    </property>
   </widget>
   <widget class="QLabel" name="notes_label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>250</y>
      <width>641</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size:20px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="image_label">
    <property name="geometry">
     <rect>
      <x>650</x>
      <y>300</y>
      <width>191</width>
      <height>71</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="timer_label">
    <property name="geometry">
     <rect>
      <x>660</x>
      <y>240</y>
      <width>121</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size:17px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="show_lvls">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>90</y>
      <width>131</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Показать уровни</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lvl_edit">
    <property name="geometry">
     <rect>
      <x>650</x>
      <y>70</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>910</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="Notes_keys"/>
 </buttongroups>
</ui>
"""

NOTES = ['do', 're', 'mi', 'fa', 'so', 'la', 'si']
NOTES_DIEZ = ['do', 're', 'fa', 'so', 'la']


class Piano(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(teamplate2)
        uic.loadUi(f, self)
        self.initUi()
        pygame.mixer.init()
        self.keys_sl = {'Q': 'do1', 'W': 're1', 'E': 'mi1', 'R': 'fa1', 'T': 'sol1', 'Y': 'la1', 'U': 'si1', 'I': 'do2',
                        'O': 're2', 'P': 'mi2', 'Z': 'fa2', 'X': 'sol2', 'C': 'la2', 'V': 'si2', '2': 'do1_diez',
                        '3': 're1_diez', '5': 'fa1_diez', '6': 'sol1_diez', '7': 'la1_diez', '9': 'do2_diez',
                        '0': 're2_diez', 'S': 'fa2_diez', 'D': 'sol2_diez', 'F': 'la2_diez'}
        self.buttons = [self.Do1, self.Re1, self.Mi1, self.Fa1, self.Sol1, self.La1, self.Si1, self.Do2, self.Re2,
                        self.Mi2, self.Fa2, self.Sol2, self.La2, self.Si2, self.Do1_diez, self.Re1_diez, self.Fa1_diez,
                        self.Sol1_diez, self.La1_diez, self.Do2_diez, self.Re2_diez, self.Fa2_diez, self.Sol2_diez,
                        self.La2_diez]
        self.initSl()
        self.initBut()
        self.lvl_in_play = False
        self.setFixedSize(841, 596)

    def initUi(self):
        self.pix_check = QPixmap('green_check.png')
        self.pix_cross = QPixmap('red_cross.png')
        self.Do1_diez.raise_()
        self.Re1_diez.raise_()
        self.Fa1_diez.raise_()
        self.Sol1_diez.raise_()
        self.La1_diez.raise_()
        self.Do2_diez.raise_()
        self.Re2_diez.raise_()
        self.Fa2_diez.raise_()
        self.Sol2_diez.raise_()
        self.La2_diez.raise_()

        self.Do1.clicked.connect(self.note_clicked)
        self.Re1.clicked.connect(self.note_clicked)
        self.Mi1.clicked.connect(self.note_clicked)
        self.Fa1.clicked.connect(self.note_clicked)
        self.Sol1.clicked.connect(self.note_clicked)
        self.La1.clicked.connect(self.note_clicked)
        self.Si1.clicked.connect(self.note_clicked)
        self.Do2.clicked.connect(self.note_clicked)
        self.Re2.clicked.connect(self.note_clicked)
        self.Mi2.clicked.connect(self.note_clicked)
        self.Fa2.clicked.connect(self.note_clicked)
        self.Sol2.clicked.connect(self.note_clicked)
        self.La2.clicked.connect(self.note_clicked)
        self.Si2.clicked.connect(self.note_clicked)
        self.Do1_diez.clicked.connect(self.note_clicked)
        self.Re1_diez.clicked.connect(self.note_clicked)
        self.Fa1_diez.clicked.connect(self.note_clicked)
        self.Sol1_diez.clicked.connect(self.note_clicked)
        self.La1_diez.clicked.connect(self.note_clicked)
        self.Do2_diez.clicked.connect(self.note_clicked)
        self.Re2_diez.clicked.connect(self.note_clicked)
        self.Fa2_diez.clicked.connect(self.note_clicked)
        self.Sol2_diez.clicked.connect(self.note_clicked)
        self.La2_diez.clicked.connect(self.note_clicked)
        self.change_btn.clicked.connect(self.change_key)

        self.stop_btn.clicked.connect(self.stop_lvl)
        self.start_lvl_btn.clicked.connect(self.start_lvl)
        self.add_lvl_btn.clicked.connect(self.add_lvl)
        self.show_lvls.clicked.connect(self.show_levels)

        self.timer = QTimer()
        self.timer.timeout.connect(self.countdown)

        self.add_lvl_btn.setIcon(QIcon('magic-wand.png'))
        self.show_lvls.setIcon(QIcon('eye.png'))
        self.start_lvl_btn.setIcon(QIcon('play.png'))
        self.stop_btn.setIcon(QIcon('stop-circle.png'))

    def countdown(self):
        if self.count > 0:
            self.count -= 1
            minutes = self.count // 60
            seconds = self.count % 60
            time_format = '{:02d}:{:02d}'.format(minutes, seconds)
            self.timer_label.setText(time_format)
            self.timer_label.show()
        else:
            self.timer.stop()
            self.timer_label.setText("Время вышло!")
            QMessageBox.information(self, 'Время вышло', 'Вы не успели пройти уровень за отведенное время')
            self.lvl_in_play = False
            self.stop_lvl()

    def initSl(self):
        file = open('config.txt', 'r', encoding='utf-8')
        lines = file.readlines()
        line = lines[0][11:-2]
        keys_list = self.remove_characters(line).split()
        for new_key, old_key in zip(keys_list, list(self.keys_sl.keys())):
            self.keys_sl[new_key] = self.keys_sl.pop(old_key)
        file.close()

    def initBut(self):
        for i in range(len(self.buttons)):
            object_ = self.buttons[i]
            if object_.objectName()[-1] == 'z':
                object_.setText(f'{list(self.keys_sl.keys())[i]}')
            else:
                object_.setText(f'\n\n\n{list(self.keys_sl.keys())[i]}')

    def stop_lvl(self):
        if self.lvl_in_play:
            self.lvl_in_play = False
            QMessageBox.information(self, 'Уровень остановлен', "Вы успешно прервали выполнение уровня")
        self.timer.stop()
        self.timer_label.hide()
        self.notes_label.hide()
        self.image_label.hide()

    def exercise_to_notes(self, ex):
        res = []
        for i in range(len(ex)):
            if ex[i:i + 2] in NOTES:
                res.append(ex[i:i + 3])
                i += 2
            elif ex[i] == 'D':
                res[-1] = res[-1] + '_diez'
        while True:
            if 'so1' in res:
                res[res.index('so1')] = 'sol1'
            if 'so2' in res:
                res[res.index('so2')] = 'sol2'
            if 'so1_diez' in res:
                res[res.index('so1_diez')] = 'sol1_diez'
            if 'so2_diez' in res:
                res[res.index('so2_diez')] = 'sol2_diez'
            if not ('so1' in res and 'so2' in res and 'so1_diez' in res and 'so2_diez' in res):
                break
        return res

    def start_lvl(self):
        if not self.lvl_in_play:
            con = sqlite3.connect('projectDB.sqlite')
            cur = con.cursor()
            self.image_label.show()
            self.lvl_in_play = True
            self.mistakes = 0
            try:
                request = cur.execute('''SELECT exercise, time from levels where id = ?''',
                                      (self.lvl_edit.text(),)).fetchall()
                self.notes_lvl = self.exercise_to_notes(request[0][0])
                self.change_notes_label()
                time = int(request[0][1])
                if time != 0:
                    self.count = time
                    self.timer.start(1000)
                con.close()
            except Exception:
                request = cur.execute('''SELECT exercise, time from levels where name = ?''',
                                      (self.lvl_edit.text(),)).fetchall()
                self.notes_lvl = self.exercise_to_notes(request[0][0])
                self.change_notes_label()
                time = int(request[0][1])
                if time != 0:
                    self.count = time
                    self.timer.start(1000)
        else:
            QMessageBox.warning(self, "Ошибка", f"Уровень уже запущен!")

    def change_notes_label(self):
        s = ''
        if len(self.notes_lvl) != 0:
            for i in range(len(self.notes_lvl)):
                s += f'{self.notes_lvl[i]}, '
            self.notes_label.show()
            self.notes_label.setText(s)
        else:
            self.end_lvl()

    def end_lvl(self):
        self.lvl_in_play = False
        self.notes_label.setText('')
        self.image_label.hide()
        self.timer.stop()
        self.timer_label.hide()
        QMessageBox.information(self, "Поздравляем", f"Вы прошли уровень {self.lvl_edit.text()}")

    def add_lvl(self):
        self.add_lvl_window = (AddLvl(self))
        self.add_lvl_window.show()

    def remove_characters(self, input_string):
        characters_to_remove = ["{", "'", ",", ":", '}']
        for char in characters_to_remove:
            input_string = input_string.replace(char, "")
        return input_string

    def keyPressEvent(self, event):
        if 0 < event.key() < 240:
            key_char = chr(event.key()).upper()
            if key_char in self.keys_sl:
                self.note_clicked(self.keys_sl[key_char])
                event.accept()
            else:
                super().keyPressEvent(event)

    def note_clicked(self, arg):
        self.scaled_pixmap1 = self.pix_check.scaled(self.image_label.size())
        self.scaled_pixmap2 = self.pix_cross.scaled(self.image_label.size())
        try:
            key = self.sender().objectName()
            note = key[0].lower() + key[1:]
            self.play(note + '.wav')
            if self.lvl_in_play:
                if note == self.notes_lvl[0]:
                    self.notes_lvl.pop(0)
                    self.change_notes_label()
                    self.image_label.setPixmap(self.scaled_pixmap1)
                else:
                    self.image_label.setPixmap(self.scaled_pixmap2)
        except AttributeError:
            self.play(arg + '.wav')
            if self.lvl_in_play:
                if arg == self.notes_lvl[0]:
                    self.notes_lvl.pop(0)
                    self.change_notes_label()
                    self.image_label.setPixmap(self.scaled_pixmap1)
                else:
                    self.image_label.setPixmap(self.scaled_pixmap2)

    def play(self, filename):
        current_directory = os.path.dirname(__file__)
        sounds_directory = os.path.join(current_directory, 'Sounds')
        sound_file_path = os.path.join(sounds_directory, filename)
        pygame.mixer.set_num_channels(1000)
        sound = pygame.mixer.Sound(sound_file_path)  # Создание объекта Sound
        channel = pygame.mixer.find_channel()  # Поиск свободного канала
        if channel:
            channel.play(sound)

    def replace_key(self, d, old_key, new_key):
        new_dict = {}
        for key, value in d.items():
            if key == old_key:
                new_dict[new_key] = value
            else:
                new_dict[key] = value
        return new_dict

    def change_key(self):
        before = self.key_before.text().upper()
        after = self.key_after.text().upper()
        try:
            if after in self.keys_sl.keys():
                raise after_in_keys
            if before in self.keys_sl.keys():
                for elem in self.buttons:
                    if elem.text().strip() == before:
                        if not elem.objectName()[-1] == 'z':
                            elem.setText(f'\n\n\n{after}')
                        else:
                            elem.setText(f'{after}')
                updated_dict = self.replace_key(self.keys_sl, before, after)
                self.keys_sl = updated_dict
        except after_in_keys:
            QMessageBox.warning(self, "Ошибка", f"Кнопка '{after}' уже используется")

    def show_levels(self):
        self.window = DatabaseTableWindow()
        self.window.show()

    def closeEvent(self, event):
        with open("config.txt", 'r') as fp:
            lines = fp.readlines()

        with open("config.txt", 'w') as fp:
            lines.insert(0, str(self.keys_sl.keys()))
            for number, line in enumerate(lines):
                if number != 1:
                    fp.write(line)


class Mistake_in_notes(Exception):
    pass

class AddLvl(QMainWindow):
    def __init__(self, parent=None):
        super(AddLvl, self).__init__(parent)
        f = io.StringIO(teamplate)
        uic.loadUi(f, self)
        self.do_btn.clicked.connect(self.note_click)
        self.re_btn.clicked.connect(self.note_click)
        self.mi_btn.clicked.connect(self.note_click)
        self.fa_btn.clicked.connect(self.note_click)
        self.so_btn.clicked.connect(self.note_click)
        self.la_btn.clicked.connect(self.note_click)
        self.si_btn.clicked.connect(self.note_click)
        self.one_btn.clicked.connect(self.note_click)
        self.two_btn.clicked.connect(self.note_click)
        self.diez_btn.clicked.connect(self.note_click)
        self.clear_btn.clicked.connect(self.clear_notes)
        self.continue_btn.clicked.connect(self.done)

    def note_click(self):
        sender = self.sender().text()
        if sender in ['1', '2']:
            self.notes_text.setText(self.notes_text.text() + sender + ' ')
        else:
            self.notes_text.setText(self.notes_text.text() + sender)

    def clear_notes(self):
        self.notes_text.setText('')

    def notes_check(self, notes):
        print(notes)
        for elem in notes:
            if elem[-1] in ['1', '2']:
                if not elem[:-1] in NOTES:
                    return f'Перед {elem[-1]} должна быть нота'
            elif elem[-1] == 'D':
                if elem[-2] in ['1', '2']:
                    if not elem[:-2] in NOTES_DIEZ:
                        return f'Нет ноты {elem[:-2]} диез!'
                else:
                    return f'Нет индекса у ноты'
            else:
                return f'Нет индекса у ноты'
        return True


    def done(self):
        notes = self.notes_text.text()
        notes = notes.replace(' ', '')
        notes_sl = {"До": "do", "Ре": 're', "Ми": 'mi', "Фа": 'fa', "Соль": 'so', "Ля": 'la', "Си": 'si'}
        res = []
        if len(notes) == 0:
            QMessageBox.warning(self, "Ошибка", f"В уровне должны быть ноты")
        else:
            while True:
                if notes[:2] in ["До", "Ре", "Ми", "Фа", "Соль", "Ля", "Си"]:
                    res.append(notes_sl[notes[:2]])
                    notes = notes[2:]
                elif notes[0] in ['1', '2']:
                    if len(res) != 0:
                        res[-1] = res[-1] + notes[0]
                        notes = notes[1:]
                else:
                    res[-1] = res[-1] + 'D'
                    notes = notes[4:]
                if len(notes) == 0:
                    break
            string_res = ''
            for elem in res:
                string_res += elem
            check = self.notes_check(res)
            if check is True:
                con = sqlite3.connect('projectDB.sqlite')
                cur = con.cursor()
                cur.execute("""INSERT INTO levels(name, exercise, time) VALUES(?, ?, ?)""",
                            (self.lvl_name.text(), string_res, self.time_spin.value()))
                QMessageBox.information(self, "Уровень добавлен", f"Вы добавили уровень {self.lvl_name.text()}")
                con.commit()
                self.close()
            else:
                QMessageBox.warning(self, 'Ошибка', f'Ошибка при вводе нот! {check}')


class DatabaseTableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("База уровней")
        self.table_widget = QTableWidget()
        self.load_data_from_database()
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_data_from_database(self):
        connection = sqlite3.connect('projectDB.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM levels")
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        self.table_widget.setRowCount(len(rows))
        self.table_widget.setColumnCount(len(column_names))
        self.table_widget.setHorizontalHeaderLabels(column_names)
        for row_index, row_data in enumerate(rows):
            for column_index, cell_data in enumerate(row_data):
                self.table_widget.setItem(row_index, column_index, QTableWidgetItem(str(cell_data)))
        connection.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Piano()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
