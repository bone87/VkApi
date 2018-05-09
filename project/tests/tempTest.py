# coding=utf-8
from time import sleep
from framework.support.commonFunctions import get_random_int
from framework.utils.email_sender import send_email_with_attach
from project.steps.messagesSteps import send_birthday_messages
from project.steps.usersSteps import search_birthday_users
from timeit import default_timer as timer
from framework.support.MyLogger import MyLogger

numbers_tokens = [
    # ["25 7214755", "f60f2697290084269401c30cc12297965909f411c681fde1b7dc2fc77daf6ffde8a04659d272f80677dbf", get_random_int(4, 8)],
    ["25 9071166", "340b0643780bd0c3f5b69e2442136a6fbecdbbebfaf50d0a191125f0a4ad4a464513737d4ae0fd03b26e7", get_random_int(8, 18)],
    ["25 9065400", "f041569b15d8fb4dbd6d8075e25aea4dd23ce24def7f2a2adf21993a2a4bae41d336fbaa0da3866833e8f", get_random_int(8, 18)],
    ["25 9062961", "b5c8fa1b2c2c24bfbd8a5c00eea2bdbf751994d53e0ebf720fdd6f04a7d453b036eadad62541885ff18d4", get_random_int(8, 18)],
    # ["25 9068942", "bab845ef83c603936dabf6f3c485162260b29c3fe8932a65c67886f201eaab403d42c401d1a19e9c0b96a", get_random_int(8, 18)],
    # ["25 9056798", "27d440d82efc30aa5bb81402ec5b2d3fbe52e47d36d412fe184cd2b7daf038c7f866ac650c420103ba043", get_random_int(8, 18)],

    ["25 7632584", "824e6bcd863c2e46b59bd3695ba1829dedafeec4594697e4d940340686dea069b85418421b227675ed896", get_random_int(8, 18)],
    ["25 7596046", "2def2fd8992e5f992b23c95d13a64055b81f7cc16a7a5dfad36084e10946b561577695bd9e751cf28265a", get_random_int(8, 18)],
    ["25 7578000", "3fb4aa5b787a9caf98a3d9ab2c78cdca652bda3ee9e3ef80eebf912c4fd0f4429370cd83964dae8799d57", get_random_int(8, 18)],
    ["25 7544404", "3e847e01dfc92e5d490e3d2773799f11ddc370d13e72b8f8ef0e1dbeaff8e34d7b69a4855bc225cdbd680", get_random_int(8, 18)],
    ["25 7512198", "2b2b15bd56850abf86f1dda6530556708d0d53ffd9b990c64ea4310f338570fbb4c7a9ec54ec4bee2dd29", get_random_int(8, 18)],

    ["25 7311641", "7760679d21f58bb60a1e2906f1804d6a30a0f937345e7c8dbe9cf641d8bcaf736e48a1f2b4f34cd94d7b9", get_random_int(8, 18)],
    ["25 7351050", "b11dcee35fbbf091e5f1a31e6bcb38fbbea8ca77c2119226d126ad3881e5052bd7232cf46335c761cbd1e", get_random_int(8, 18)],
    ["25 7369155", "1f14675ac6c2a063b3b6dc867165fb33adc3959821da2c1ce4a9ba1d9b383f0799f4b5dbdbdbc03a42fd5", get_random_int(8, 18)],
    ["25 7514961", "cc8c4ca584547e8a21c88db19a7d8372a5342c799c4db18cf19e80c98d16979b8a148a5c13f207bfd3525", get_random_int(8, 18)],
    ["25 7409700", "8f8682270b315981b6613296e7de022f1ea9f0db1a45bca4751df04c9a07d15994bb281b913697a7486c5", get_random_int(8, 18)],

    ["25 9619978", "428a4c4760cf4b5a12331b878572ce15c22a81154d07b37b1f8a87b71cbb57ba5253af501471b7e6c48c5", get_random_int(8, 18)],
    ["25 9619974", "2265aef190052a3870c8b2f855d96bd7eb8e9266e3541bc056b61430925155fe7cde7191d223da17845f4", get_random_int(8, 18)],
    ["25 9619971", "a39e8766eacd5f531319db0a29cf2a5b5b24830eada43d7c508e75f75b6ac1f61c3a7f1502318c40390ba", get_random_int(8, 18)],
    ["25 9619957", "12bdc6adbb62303bcfce61f97262247fad069338554b40da818c1c22efa7e871155e658b0fa05df498cdc", get_random_int(8, 18)],
    ["25 9619950", "87197e00988a68da74e59ff7a03516ddaaa1de1823e44085734307f2a0ad1bf1d2f6e89654740c932577e", get_random_int(8, 18)],

    ["25 7603212", "a438ffac5cc8d13981d8ac09bba4a841e82de68110b52ac7613bf00ff1449afaa19d25361d76c5976b5c5", get_random_int(8, 18)],
    ["25 7653589", "4a6c66a55b625fb380378ad7da485560ded58c316462962b20ab417480b82588c973960f68f2106065ea0", get_random_int(8, 18)],
    ["25 7647262", "350da5697a3b19f7b2d6017cfb42653a102da2f2bde2168e5a9e7f9dd3dcfdffe856e3bb586be6a465aac", get_random_int(8, 18)],
    ["25 7617233", "9c880a39b1cf5c7419442da504ce5e87f9020955d66220dcd18b40bf532775e279c83365e60255a29e1d6", get_random_int(8, 18)],
    ["25 7628934", "a36441eb0265578fc29fb79ca2038fce7e5f24a462003d4f3cc06b57d408cea3b01f533c9f97b77289869", get_random_int(8, 18)],

    # ["25 7329516", "c9e782e2e22da7e83d8e03f6c19de0f5c79043239aeb17582e1acca2c24f28776250f1c2a5b52ff63851a", get_random_int(8, 18)],
    ["25 7559314", "af9b06edf0d78f6857b6ea54de3341dd8814313aa4049b38451423f5bc01eb1387fdc2c05ac111e95e171", get_random_int(8, 18)],
    ["25 7537018", "6feca122c433c81cdd70c250de9382b735c80a49ac37109ddfa7415716e5093eaac1b3d9a7353052b2f60", get_random_int(8, 18)],
    ["25 7422821", "a8fa386ca7bf64908c60c007672cb6a9509c8790344ff8165f227edf1dfb44de171d1076423e8d4fd4af9", get_random_int(8, 18)],
    ["25 7390452", "2c234a06af3f34cb550e042a4db0031f578b59a9ebc463d11fed7015442029c91cad6547374c844100f1b", get_random_int(8, 18)],

    ["25 9631419", "a0a2f633469a4dd77f065ad89fd22579c786676b92b53a3603a92aee573cf0ffc2ee22c0089516654a3f4", get_random_int(8, 18)],
    ["25 9631413", "353f16c4163edb1cf0efa992470b88d52ebe98c8801ff09fe82c8da26e8ea1cb69858aab5da0a77e54703", get_random_int(8, 18)],
    ["25 9631408", "c6c88a6fa7f520d8d6bfb454524645fa3d564ed96eae8ede8b7439dba9565f09241a6ae1d7056694ff29f", get_random_int(8, 18)],
    ["25 9631390", "473474c920a663d013a17f062954e6fe5c492b2f22460c51d629e6b871b83ebad231e1c6b3d9e9b34dce6", get_random_int(8, 18)],
    ["25 9631404", "a40abe718d5dfcb4cb2a832e00e093c32bdd5440de317ddade6b3abf2b820d8118d346930d800ceb89361", get_random_int(8, 18)]

]

logger = MyLogger()


def run_sender(age_from, age_to):
    start = timer()
    sec = get_random_int(60, 1000)
    logger.log_info('Задержка: {min}min {sec}s.'.format(min=sec//60, sec=sec % 60))
    sleep(sec)
    offset = 0
    count = 0
    status = 'PASS'
    message = ''
    try:
        for item in numbers_tokens:
            logger.log_step(item[0])
            logger.log_info('Смещение: {offset}.'.format(offset=offset))
            users = search_birthday_users(token=item[1], offset=offset, age_from=age_from, age_to=age_to)
            send_count = send_birthday_messages(token=item[1], users=users, max_count=item[2])
            count = count + send_count
            offset = offset + 30
            sec = get_random_int(60, 200)
            logger.log_info('Задержка перед сменой номера: {min}min {sec}s.'.format(min=sec // 60, sec=sec % 60))
            sleep(sec)
        logger.log_info('')
        logger.log_info('Всего отправлено сообщений: {count}. Среднее значение: {mid}.'.format(count=count, mid=count/len(numbers_tokens)))
    except Exception as error:
        status = 'FAIL'
        logger.log_pretty_json(json_message=error.args)
        assert False
    finally:
        end = timer()
        duration_sec = end - start
        duration_min = duration_sec // 60
        sec_rest = duration_sec % 60
        duration_hours = duration_min // 60
        min_rest = duration_min % 60

        duration_str = '{hours}h {min}min {sec}s'.format(hours=int(duration_hours),
                                                         min=int(min_rest),
                                                         sec=int(sec_rest))
        message = 'Duration: {duration}\nCount: {count}'.format(duration=str(duration_str),
                                                                count=count) \
                  + message
        logger.__del__()
        attached_file = logger.file_name
        send_email_with_attach(message=message,
                               attached_file=attached_file,
                               subject='{status}. {count} messages.'.format(status=status,
                                                                            count=count))


run_sender(24, 45)
