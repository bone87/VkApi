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
    ["25 9071166", "d7d021d6f7e9315692829c9aea08637f2abe615e5d42a70b7d79f87b53679bb69f38265bcfcf313664d96", get_random_int(10, 13)],
    ["25 9005346", "84ac09b524802cd6143cefe519ad3965e30f08a8ff53999ed99bb213a0952af932a90c0a1172ee6db62da", get_random_int(10, 13)],
    ["25 9062961", "9e2ae486f5d2633e68580ea8d8573c1371992aeadeadcd7281894b2a496c1bf5c4cef40df449c6e924b5b", get_random_int(10, 13)],
    ["25 9068942", "dc568b2d1365acc0a60bcf7fd9317962f0992d2bc2178568f940c64ef713d5b92630194f4ce0fb7e958dd", get_random_int(10, 13)],
    ["25 9056798", "ed185560b68d089c1db724d02a51ba5e5f91874a6eca3bd726e3d837914e48767092ec492e74ed2f0c78b", get_random_int(10, 13)],

    ["25 7632584", "b3335c4bd57eec47a0591c2ab5eebf30075bb3cc536feca13de2e3196a56401af6be69b2099c61f614485", get_random_int(10, 13)],
    ["25 7596046", "25b6071d767d08f664f6e482d18e3bf65a74d9abf8ae3ad9bbaac0e05c29882fe0019a898da3fdbb74acb", get_random_int(10, 13)],
    ["25 9008203", "d495d4f13581f222369857e9995e3177757f8e3bb59d4cd3293b5f952b9226d9a141f0c98b3d8d4b72a8d", get_random_int(10, 13)],
    ["25 7544404", "3e847e01dfc92e5d490e3d2773799f11ddc370d13e72b8f8ef0e1dbeaff8e34d7b69a4855bc225cdbd680", get_random_int(10, 13)],
    # ["25 9018087", "2b2b15bd56850abf86f1dda6530556708d0d53ffd9b990c64ea4310f338570fbb4c7a9ec54ec4bee2dd29", get_random_int(10, 13)],

    ["25 7311641", "4124b4416e2390b8595f75edb89e5be62eea6fab094e8acef61e8db96688317fe5ee717e7c465904e8dde", get_random_int(10, 13)],
    ["25 7351050", "b11dcee35fbbf091e5f1a31e6bcb38fbbea8ca77c2119226d126ad3881e5052bd7232cf46335c761cbd1e", get_random_int(10, 13)],
    ["25 7369155", "7d76176e518d429a37d93877cb49423c3847e9c227218eded797593fa885a7b75006066cb4e3e9cef7d52", get_random_int(10, 13)],
    ["25 7514961", "cc8c4ca584547e8a21c88db19a7d8372a5342c799c4db18cf19e80c98d16979b8a148a5c13f207bfd3525", get_random_int(10, 13)],
    ["25 9017225", "05c8fc77ab25cd1d21b80f4caf1ec3faad594c2467660a0113df2e2eec44cc93c58d1a7b74e1ad8adfa16", get_random_int(10, 13)],

    ["25 9619978", "428a4c4760cf4b5a12331b878572ce15c22a81154d07b37b1f8a87b71cbb57ba5253af501471b7e6c48c5", get_random_int(10, 13)],
    ["25 9619974", "46c92bb375f1078e2bb2138bbb1adb15aa76fcd721b7909cc47f39bc8a5019bedf6eeda4960205e30bfd4", get_random_int(10, 13)],
    ["25 9619971", "1be5829832f6faaeebe6b1bec3a21bb33e53d96b8bdd4e0206672e3c667a3ee43ce6fc69c8e2d00b4b938", get_random_int(10, 13)],
    ["25 9619957", "12bdc6adbb62303bcfce61f97262247fad069338554b40da818c1c22efa7e871155e658b0fa05df498cdc", get_random_int(10, 13)],
    ["25 9619950", "2e64cfd55d385d2b495f440ee8a148dec0996f5c88acd3f219ca7f6574e25c6d33fd5855a09826e2aabb5", get_random_int(10, 13)],

    ["25 7603212", "92ecfbcfdd5deccad0e5e7054270b9ac864b24c9a898b801d70ad4fe3f4901c29b0eed5d52ffae4fc65e6", get_random_int(10, 13)],
    ["25 7653589", "8a8ebc443e258aeb9d24ac1fe98a868d7ad5b4ed3f91b9661b1cfcdf08758e167bd5e2b3cd5703d2d29ed", get_random_int(10, 13)],
    ["25 7647262", "344b308a2ad4357f7847090040e8f9bb51339bcb20114934ed895023eb9d4f4aaa8bdc31a818dcaff135b", get_random_int(10, 13)],
    ["25 7617233", "ddd8dfc1283aedc7cc08a63af203fa295805be2470167f69b52a88ffa869d704c27da90f1a70a28606c6d", get_random_int(10, 13)],
    ["25 7628934", "a36441eb0265578fc29fb79ca2038fce7e5f24a462003d4f3cc06b57d408cea3b01f533c9f97b77289869", get_random_int(10, 13)],

    ["25 7329516", "096a82237bb2c4c0178fef08b4daf437611f714975cf446562d64681a003f1824c70f8429d4c23342d054", get_random_int(10, 13)],
    ["25 7559314", "2ec114fcebb65072d9a3204759640a5a5fa066c133e15773d1ed28dfd3f342a5f8ea1282027a96ee93be7", get_random_int(10, 13)],
    ["25 7537018", "3509d89b0944bd6f19fdfd1c1623d29de213e5107358214f6a5175231015e6ceac95eb8d9df0118312471", get_random_int(10, 13)],
    ["25 7422821", "a8fa386ca7bf64908c60c007672cb6a9509c8790344ff8165f227edf1dfb44de171d1076423e8d4fd4af9", get_random_int(10, 13)],
    ["25 7390452", "d040b24ddd00d03dff30460c954e011be2a4f46853cd904d7a969b74336fe46bb5c23e60e4821fef83875", get_random_int(10, 13)],

    ["25 9631419", "a0a2f633469a4dd77f065ad89fd22579c786676b92b53a3603a92aee573cf0ffc2ee22c0089516654a3f4", get_random_int(10, 13)],
    ["25 9631413", "1b434c58cc10e1a9e4332ee5f2c2b552e7febe1a6c50b76ce979f6e19ded79db84d3d9450b47bce7b8a25", get_random_int(10, 13)],
    ["25 9631408", "19df414726e65a180b9c04f01f77556789fbd65e7efc2c3a0e84464448064006b833b7a3c39e13ac84af4", get_random_int(10, 13)],
    ["25 9631390", "473474c920a663d013a17f062954e6fe5c492b2f22460c51d629e6b871b83ebad231e1c6b3d9e9b34dce6", get_random_int(10, 13)],
    ["25 9631404", "4b5a15a56e6c91f4ce91636dc4895ac392889f387911d410311272a39be61e724700340d55977f6f71aef", get_random_int(10, 13)]

]

logger = MyLogger()


def run_sender(age_from, age_to):
    start = timer()
    sec = get_random_int(60, 1000)
    logger.log_info(u'Задержка: {min}min {sec}s.'.format(min=sec//60, sec=sec % 60))
    sleep(sec)
    offset = 0
    count = 0
    status = 'PASS'
    message = ''
    try:
        for item in numbers_tokens:
            logger.log_step(item[0])
            logger.log_info(u'Смещение: {offset}.'.format(offset=offset))
            users = search_birthday_users(token=item[1], offset=offset, age_from=age_from, age_to=age_to)
            send_count = send_birthday_messages(token=item[1], users=users, max_count=item[2])
            count = count + send_count
            offset = offset + 30
            sec = get_random_int(60, 200)
            logger.log_info(u'Задержка перед сменой номера: {min}min {sec}s.'.format(min=sec // 60, sec=sec % 60))
            sleep(sec)
        logger.log_info('')
        logger.log_info(u'Всего отправлено сообщений: {count}. Среднее значение: {mid}.'.format(count=count, mid=count/len(numbers_tokens)))
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


run_sender(24, 50)
