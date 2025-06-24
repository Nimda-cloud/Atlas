from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QHBoxLayout, QMessageBox, QFrame
from PySide6.QtCore import Qt
from ui_qt.plugin_manager import PluginManager
from ui_qt.i18n import _

class PluginsModule(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("PluginsModule")
        self.plugin_manager = None
        self.tool_widgets = []
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        self.title = QLabel(_("🧩 Plugins"))
        self.title.setStyleSheet("color: #ff00c8; font-size: 22px; font-weight: bold; letter-spacing: 1px;")
        layout.addWidget(self.title)

        self.list = QListWidget()
        self.list.setStyleSheet("background: #181c20; color: #fff; border: 1px solid #ff00c8; border-radius: 8px; font-size: 15px;")
        self.list.setDragDropMode(self.list.InternalMove)
        layout.addWidget(self.list, stretch=1)

        btns = QHBoxLayout()
        self.activate_btn = QPushButton(_("Activate"))
        self.activate_btn.setStyleSheet("background: #ff00c8; color: #181c20; font-weight: bold; border-radius: 6px; padding: 6px 18px;")
        self.activate_btn.clicked.connect(self.activate_plugin)
        btns.addWidget(self.activate_btn)
        self.deactivate_btn = QPushButton(_("Deactivate"))
        self.deactivate_btn.setStyleSheet("background: #23272e; color: #ff00c8; border-radius: 6px; padding: 6px 18px;")
        self.deactivate_btn.clicked.connect(self.deactivate_plugin)
        btns.addWidget(self.deactivate_btn)
        self.reload_btn = QPushButton(_("Reload Plugins"))
        self.reload_btn.setStyleSheet("background: #23272e; color: #ff00c8; border-radius: 6px; padding: 6px 18px; font-style: italic;")
        self.reload_btn.clicked.connect(self.reload_plugins)
        btns.addWidget(self.reload_btn)
        layout.addLayout(btns)

        self.tools_frame = QFrame()
        self.tools_layout = QVBoxLayout(self.tools_frame)
        self.tools_layout.setContentsMargins(0, 10, 0, 0)
        layout.addWidget(self.tools_frame)

    def update_ui(self):
        self.title.setText(_("🧩 Plugins"))
        self.activate_btn.setText(_("Activate"))
        self.deactivate_btn.setText(_("Deactivate"))
        self.reload_btn.setText(_("Reload Plugins"))

    def set_plugin_manager(self, plugin_manager):
        self.plugin_manager = plugin_manager
        self.update_plugins()

    def update_plugins(self):
        self.list.clear()
        if not self.plugin_manager:
            return
        for name, plugin in self.plugin_manager.plugins.items():
            status = _( "(active)") if plugin.active else _( "(inactive)")
            self.list.addItem(f"{name} {status}")
        self.update_tools()

    def update_tools(self):
        for w in self.tool_widgets:
            w.setParent(None)
        self.tool_widgets.clear()
        if not self.plugin_manager:
            return
        for name, plugin in self.plugin_manager.plugins.items():
            if plugin.active and hasattr(plugin, 'get_widget'):
                widget = plugin.get_widget(self)
                if widget:
                    self.tools_layout.addWidget(widget)
                    self.tool_widgets.append(widget)

    def activate_plugin(self):
        row = self.list.currentRow()
        if row >= 0 and self.plugin_manager:
            name = self.list.item(row).text().split()[0]
            self.plugin_manager.activate_plugin(name)
            self.update_plugins()
        else:
            QMessageBox.warning(self, _( "Activate Plugin"), _( "Select a plugin to activate."))

    def deactivate_plugin(self):
        row = self.list.currentRow()
        if row >= 0 and self.plugin_manager:
            name = self.list.item(row).text().split()[0]
            self.plugin_manager.deactivate_plugin(name)
            self.update_plugins()
        else:
            QMessageBox.warning(self, _( "Deactivate Plugin"), _( "Select a plugin to deactivate."))

    def reload_plugins(self):
        if self.plugin_manager:
            self.plugin_manager.reload_all_plugins()
            self.update_plugins()
            QMessageBox.information(self, _( "Reload Plugins"), _( "All plugins reloaded."))

    def search(self, query):
        """Повертає список словників: {'label': ім'я + опис, 'key': ім'я}"""
        results = []
        if not self.plugin_manager:
            return results
        for name, plugin in self.plugin_manager.plugins.items():
            info = plugin.info()
            label = f"{info.get('name', name)}: {info.get('description', '')}"
            if query.lower() in label.lower():
                results.append({'label': label, 'key': name})
        return results

    def select_by_key(self, key):
        for i in range(self.list.count()):
            name = self.list.item(i).text().split()[0]
            if name == key:
                self.list.setCurrentRow(i)
                self.list.scrollToItem(self.list.item(i))
                break 