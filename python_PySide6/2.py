import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='定时器示例', width=400, height=200)

counter = 0

def timer_callback(sender):
    global counter
    counter += 1
    dpg.set_value("counter", f"计数: {counter}")

with dpg.window(label="主窗口"):
    dpg.add_text("计数器应用")
    dpg.add_text("", tag="counter")
    dpg.add_button(label="开始", callback=lambda: dpg.configure_item("my_timer", show=True))
    dpg.add_button(label="停止", callback=lambda: dpg.configure_item("my_timer", show=False))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()