# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options_metadata.ui'
#
# Created: Fri May 24 09:20:07 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MetadataOptionsPage(object):
    def setupUi(self, MetadataOptionsPage):
        MetadataOptionsPage.setObjectName(_fromUtf8("MetadataOptionsPage"))
        MetadataOptionsPage.resize(423, 553)
        self.verticalLayout = QtGui.QVBoxLayout(MetadataOptionsPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.metadata_groupbox = QtGui.QGroupBox(MetadataOptionsPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.metadata_groupbox.sizePolicy().hasHeightForWidth())
        self.metadata_groupbox.setSizePolicy(sizePolicy)
        self.metadata_groupbox.setMinimumSize(QtCore.QSize(397, 135))
        self.metadata_groupbox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.metadata_groupbox.setObjectName(_fromUtf8("metadata_groupbox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.metadata_groupbox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.translate_artist_names = QtGui.QCheckBox(self.metadata_groupbox)
        self.translate_artist_names.setObjectName(_fromUtf8("translate_artist_names"))
        self.verticalLayout_3.addWidget(self.translate_artist_names)
        self.artist_locale = QtGui.QComboBox(self.metadata_groupbox)
        self.artist_locale.setObjectName(_fromUtf8("artist_locale"))
        self.verticalLayout_3.addWidget(self.artist_locale)
        self.standardize_artists = QtGui.QCheckBox(self.metadata_groupbox)
        self.standardize_artists.setObjectName(_fromUtf8("standardize_artists"))
        self.verticalLayout_3.addWidget(self.standardize_artists)
        self.convert_punctuation = QtGui.QCheckBox(self.metadata_groupbox)
        self.convert_punctuation.setObjectName(_fromUtf8("convert_punctuation"))
        self.verticalLayout_3.addWidget(self.convert_punctuation)
        self.release_ars = QtGui.QCheckBox(self.metadata_groupbox)
        self.release_ars.setObjectName(_fromUtf8("release_ars"))
        self.verticalLayout_3.addWidget(self.release_ars)
        self.track_ars = QtGui.QCheckBox(self.metadata_groupbox)
        self.track_ars.setObjectName(_fromUtf8("track_ars"))
        self.verticalLayout_3.addWidget(self.track_ars)
        self.folksonomy_tags = QtGui.QCheckBox(self.metadata_groupbox)
        self.folksonomy_tags.setObjectName(_fromUtf8("folksonomy_tags"))
        self.verticalLayout_3.addWidget(self.folksonomy_tags)
        self.verticalLayout.addWidget(self.metadata_groupbox)
        self.custom_fields_groupbox = QtGui.QGroupBox(MetadataOptionsPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_fields_groupbox.sizePolicy().hasHeightForWidth())
        self.custom_fields_groupbox.setSizePolicy(sizePolicy)
        self.custom_fields_groupbox.setMinimumSize(QtCore.QSize(397, 0))
        self.custom_fields_groupbox.setObjectName(_fromUtf8("custom_fields_groupbox"))
        self.gridlayout = QtGui.QGridLayout(self.custom_fields_groupbox)
        self.gridlayout.setSpacing(2)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_6 = QtGui.QLabel(self.custom_fields_groupbox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout.addWidget(self.label_6, 0, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.custom_fields_groupbox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridlayout.addWidget(self.label_7, 2, 0, 1, 2)
        self.nat_name = QtGui.QLineEdit(self.custom_fields_groupbox)
        self.nat_name.setObjectName(_fromUtf8("nat_name"))
        self.gridlayout.addWidget(self.nat_name, 3, 0, 1, 1)
        self.nat_name_default = QtGui.QPushButton(self.custom_fields_groupbox)
        self.nat_name_default.setObjectName(_fromUtf8("nat_name_default"))
        self.gridlayout.addWidget(self.nat_name_default, 3, 1, 1, 1)
        self.va_name_default = QtGui.QPushButton(self.custom_fields_groupbox)
        self.va_name_default.setObjectName(_fromUtf8("va_name_default"))
        self.gridlayout.addWidget(self.va_name_default, 1, 1, 1, 1)
        self.va_name = QtGui.QLineEdit(self.custom_fields_groupbox)
        self.va_name.setObjectName(_fromUtf8("va_name"))
        self.gridlayout.addWidget(self.va_name, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.custom_fields_groupbox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_6.setBuddy(self.va_name_default)
        self.label_7.setBuddy(self.nat_name_default)

        self.retranslateUi(MetadataOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(MetadataOptionsPage)
        MetadataOptionsPage.setTabOrder(self.translate_artist_names, self.artist_locale)
        MetadataOptionsPage.setTabOrder(self.artist_locale, self.standardize_artists)
        MetadataOptionsPage.setTabOrder(self.standardize_artists, self.convert_punctuation)
        MetadataOptionsPage.setTabOrder(self.convert_punctuation, self.release_ars)
        MetadataOptionsPage.setTabOrder(self.release_ars, self.track_ars)
        MetadataOptionsPage.setTabOrder(self.track_ars, self.folksonomy_tags)
        MetadataOptionsPage.setTabOrder(self.folksonomy_tags, self.va_name)
        MetadataOptionsPage.setTabOrder(self.va_name, self.va_name_default)
        MetadataOptionsPage.setTabOrder(self.va_name_default, self.nat_name)
        MetadataOptionsPage.setTabOrder(self.nat_name, self.nat_name_default)

    def retranslateUi(self, MetadataOptionsPage):
        self.metadata_groupbox.setTitle(_("Metadata"))
        self.translate_artist_names.setText(_("Translate artist names to this locale where possible:"))
        self.standardize_artists.setText(_("Use standardized artist names"))
        self.convert_punctuation.setText(_("Convert Unicode punctuation characters to ASCII"))
        self.release_ars.setText(_("Use release relationships"))
        self.track_ars.setText(_("Use track relationships"))
        self.folksonomy_tags.setText(_("Use folksonomy tags as genre"))
        self.custom_fields_groupbox.setTitle(_("Custom Fields"))
        self.label_6.setText(_("Various artists:"))
        self.label_7.setText(_("Non-album tracks:"))
        self.nat_name_default.setText(_("Default"))
        self.va_name_default.setText(_("Default"))

