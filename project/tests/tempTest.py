# coding=utf-8
from time import sleep
from framework.support.commonFunctions import get_random_int
from framework.utils.email_sender import send_email_with_attach
from project.steps.messagesSteps import send_birthday_messages
from project.steps.usersSteps import search_birthday_users
from timeit import default_timer as timer
from framework.support.MyLogger import MyLogger

numbers_tokens = [
    ["25 7214755", "a3383acc5f71ac8b6b0e88184f10b0084625ab832f84f3e72fb20e6e858b1c2b11f9f98ffca7e011bd398", get_random_int(14, 18)],
    ["25 9071166", "340b0643780bd0c3f5b69e2442136a6fbecdbbebfaf50d0a191125f0a4ad4a464513737d4ae0fd03b26e7", get_random_int(14, 18)],
    ["25 9065400", "f041569b15d8fb4dbd6d8075e25aea4dd23ce24def7f2a2adf21993a2a4bae41d336fbaa0da3866833e8f", get_random_int(14, 18)],
    # ["25 9062961", "b5c8fa1b2c2c24bfbd8a5c00eea2bdbf751994d53e0ebf720fdd6f04a7d453b036eadad62541885ff18d4", get_random_int(14, 18)],
    ["25 9068942", "ccae722d41b078eea221ba7364c0aa47f4cc7f727a5d3e82f5261ca6764f4b49088e2238ff6122addf73c", get_random_int(14, 18)],
    ["25 9056798", "c97f4022af80e1de81f60f5905068c9ed5ec83242f52dab670e3e4ab24033cb5968fa624edba82f6c6e1e", get_random_int(14, 18)],
    #
    ["25 7632584", "998aac3cf32cbf901a98720e7091839c6b708fd95535bb52b4c2ad55ad3c83278b194d59bd7b247056631", get_random_int(14, 18)],
    ["25 7596046", "2def2fd8992e5f992b23c95d13a64055b81f7cc16a7a5dfad36084e10946b561577695bd9e751cf28265a", get_random_int(14, 18)],
    ["25 7578000", "cf14583ea9f67746d39ae41e202dfe981195cdf7cb192a24b56230361ca5b468b1b896d9ec3d71e2137b2", get_random_int(14, 18)],
    ["25 7544404", "3e847e01dfc92e5d490e3d2773799f11ddc370d13e72b8f8ef0e1dbeaff8e34d7b69a4855bc225cdbd680", get_random_int(14, 18)],
    # ["25 7512198", "2b2b15bd56850abf86f1dda6530556708d0d53ffd9b990c64ea4310f338570fbb4c7a9ec54ec4bee2dd29", get_random_int(14, 18)],

    ["25 7311641", "728de0d39c92ddec5d292956e0c3152a4abbebd6111b4858b0469a110f470fe60b2426b05faae3dcdcf26", get_random_int(14, 18)],
    ["25 7351050", "b11dcee35fbbf091e5f1a31e6bcb38fbbea8ca77c2119226d126ad3881e5052bd7232cf46335c761cbd1e", get_random_int(14, 18)],
    ["25 7369155", "d3f5886cd8bafe59ccfe0068732c19ef573d0c4393e32018082ec3b7fbda066d1cd603788f437076d6045", get_random_int(14, 18)],
    ["25 7514961", "cc8c4ca584547e8a21c88db19a7d8372a5342c799c4db18cf19e80c98d16979b8a148a5c13f207bfd3525", get_random_int(14, 18)],
    ["25 7409700", "8f8682270b315981b6613296e7de022f1ea9f0db1a45bca4751df04c9a07d15994bb281b913697a7486c5", get_random_int(14, 18)],

    ["25 9619978", "33c8d3d5100713b0c2db430eb98c956509e07440215ddb11fddb535d1fee08aa9b1b8247c557320a166e3", get_random_int(14, 18)],
    ["25 9619974", "2265aef190052a3870c8b2f855d96bd7eb8e9266e3541bc056b61430925155fe7cde7191d223da17845f4", get_random_int(14, 18)],
    ["25 9619971", "9ec03087e21243225aa282f49084c44ebba17119e980cdc60ec1e4249fbc75b9d07bd2134131eadd00b90", get_random_int(14, 18)],
    ["25 9619957", "b0ca35b568b04ed637ca835d4d285c390cecb67c24641b8a385b661efcc61621045b0bd8dd879d8bf8e24", get_random_int(14, 18)],
    ["25 9619950", "87197e00988a68da74e59ff7a03516ddaaa1de1823e44085734307f2a0ad1bf1d2f6e89654740c932577e", get_random_int(14, 18)],

    ["25 7603212", "a438ffac5cc8d13981d8ac09bba4a841e82de68110b52ac7613bf00ff1449afaa19d25361d76c5976b5c5", get_random_int(14, 18)],
    ["25 7653589", "cb295b1b9ef33d0565bc0e5ee891d938c2765a26b1884bddd0bef84cda2367b5632e432821d10fb66e0d2", get_random_int(14, 18)],
    ["25 7647262", "350da5697a3b19f7b2d6017cfb42653a102da2f2bde2168e5a9e7f9dd3dcfdffe856e3bb586be6a465aac", get_random_int(14, 18)],
    ["25 7617233", "9c880a39b1cf5c7419442da504ce5e87f9020955d66220dcd18b40bf532775e279c83365e60255a29e1d6", get_random_int(14, 18)],
    ["25 7628934", "a36441eb0265578fc29fb79ca2038fce7e5f24a462003d4f3cc06b57d408cea3b01f533c9f97b77289869", get_random_int(14, 18)],

    ["25 7329516", "5f7ed5ba39b90d4ed1c4861878b65faa2515780c1d226da56f7bcbffc142b735472aafda01d8199598a6f", get_random_int(14, 18)],
    ["25 7559314", "af9b06edf0d78f6857b6ea54de3341dd8814313aa4049b38451423f5bc01eb1387fdc2c05ac111e95e171", get_random_int(14, 18)],
    ["25 7537018", "6feca122c433c81cdd70c250de9382b735c80a49ac37109ddfa7415716e5093eaac1b3d9a7353052b2f60", get_random_int(14, 18)],
    ["25 7422821", "a8fa386ca7bf64908c60c007672cb6a9509c8790344ff8165f227edf1dfb44de171d1076423e8d4fd4af9", get_random_int(14, 18)],
    ["25 7390452", "2c234a06af3f34cb550e042a4db0031f578b59a9ebc463d11fed7015442029c91cad6547374c844100f1b", get_random_int(14, 18)],

    ["25 9631419", "255b525851c883ab82ed981a123ff60ab709d9214dea3ecc472e01b3ab5cec32564385839a10f91176d8d", get_random_int(4, 8)],
    ["25 9631413", "353f16c4163edb1cf0efa992470b88d52ebe98c8801ff09fe82c8da26e8ea1cb69858aab5da0a77e54703", get_random_int(4, 8)],
    ["25 9631408", "c6c88a6fa7f520d8d6bfb454524645fa3d564ed96eae8ede8b7439dba9565f09241a6ae1d7056694ff29f", get_random_int(4, 8)]

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


# run_sender(24, 40)
