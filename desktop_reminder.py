from plyer import notification
import pywhatkit as kit
class msg:
    def whatsapp(self):
        number = input("Mobile No:")
        msg = input('Message')
        time = int(input("Time:"))
        minute = int(input("Minute:"))
        kit.sendwhatmsg(number,msg,time,minute)

    def desktop_notifications(self):
        notification_title = 'Message'
        notification_msg = "Message sent successfully.."

        notification.notify(
            title = notification_title,
            message = notification_msg,
            app_icon = None,
            timeout  = 10,
            toast = False
        )

message = msg()
a = False
b = True

try:
    if b == True:
        message.whatsapp()
        print("Message delivered successfully!!!")
        a = True
        if a == True:
            message.desktop_notifications()
        else:
            print("Something went wrong")
    else:
        print("error")

except Exception as e:
    print(e,'eee')