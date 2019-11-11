from wxpy import *
# 初始化机器人，启用缓存保存登录状态，下次不用扫码。
bot = Bot(cache_path=True)
#注册消息接收监听器
@bot.register()
#接收好友、群聊、公众号的信息输出
def print_others(msg):
    print(msg)
#回复消息msg.reply("hello world")
#堵塞线程，在线接收。
embed()
