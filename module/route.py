from module import api
# 引入WeiXin_Post_Text
from module.WeChat.text_content import WeiXin_Post_Text
from module.WeChat.text_content import WeiXin_Post_Text_Card

# 注册flask result api 路由
api.add_resource(WeiXin_Post_Text, "/api/Wechat/text/")
api.add_resource(WeiXin_Post_Text_Card, "/api/Wechat/text_card/")
