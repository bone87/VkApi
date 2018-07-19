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
    ["25 9071166", "d7d021d6f7e9315692829c9aea08637f2abe615e5d42a70b7d79f87b53679bb69f38265bcfcf313664d96", get_random_int(8, 18)],
    ["25 9065400", "f041569b15d8fb4dbd6d8075e25aea4dd23ce24def7f2a2adf21993a2a4bae41d336fbaa0da3866833e8f", get_random_int(8, 18)],
    ["25 9062961", "b5c8fa1b2c2c24bfbd8a5c00eea2bdbf751994d53e0ebf720fdd6f04a7d453b036eadad62541885ff18d4", get_random_int(8, 18)],
    ["25 9068942", "bab845ef83c603936dabf6f3c485162260b29c3fe8932a65c67886f201eaab403d42c401d1a19e9c0b96a", get_random_int(8, 18)],
    ["25 9056798", "c8f86c6ae4b298121f8249ca738b96dc2e447f99bb070ed81d9059d985468313c73cb9ab1ec33c53ad772", get_random_int(8, 18)],

    ["25 7632584", "824e6bcd863c2e46b59bd3695ba1829dedafeec4594697e4d940340686dea069b85418421b227675ed896", get_random_int(8, 18)],
    ["25 7596046", "2def2fd8992e5f992b23c95d13a64055b81f7cc16a7a5dfad36084e10946b561577695bd9e751cf28265a", get_random_int(8, 18)],
    ["25 7578000", "3fb4aa5b787a9caf98a3d9ab2c78cdca652bda3ee9e3ef80eebf912c4fd0f4429370cd83964dae8799d57", get_random_int(8, 18)],
    ["25 7544404", "3e847e01dfc92e5d490e3d2773799f11ddc370d13e72b8f8ef0e1dbeaff8e34d7b69a4855bc225cdbd680", get_random_int(8, 18)],
    ["25 7512198", "2b2b15bd56850abf86f1dda6530556708d0d53ffd9b990c64ea4310f338570fbb4c7a9ec54ec4bee2dd29", get_random_int(8, 18)],

    ["25 7311641", "4124b4416e2390b8595f75edb89e5be62eea6fab094e8acef61e8db96688317fe5ee717e7c465904e8dde", get_random_int(8, 18)],
    ["25 7351050", "b11dcee35fbbf091e5f1a31e6bcb38fbbea8ca77c2119226d126ad3881e5052bd7232cf46335c761cbd1e", get_random_int(8, 18)],
    ["25 7369155", "7d76176e518d429a37d93877cb49423c3847e9c227218eded797593fa885a7b75006066cb4e3e9cef7d52", get_random_int(8, 18)],
    ["25 7514961", "cc8c4ca584547e8a21c88db19a7d8372a5342c799c4db18cf19e80c98d16979b8a148a5c13f207bfd3525", get_random_int(8, 18)],
    ["25 7409700", "8f8682270b315981b6613296e7de022f1ea9f0db1a45bca4751df04c9a07d15994bb281b913697a7486c5", get_random_int(8, 18)],

    ["25 9619978", "428a4c4760cf4b5a12331b878572ce15c22a81154d07b37b1f8a87b71cbb57ba5253af501471b7e6c48c5", get_random_int(8, 18)],
    ["25 9619974", "2265aef190052a3870c8b2f855d96bd7eb8e9266e3541bc056b61430925155fe7cde7191d223da17845f4", get_random_int(8, 18)],
    ["25 9619971", "a39e8766eacd5f531319db0a29cf2a5b5b24830eada43d7c508e75f75b6ac1f61c3a7f1502318c40390ba", get_random_int(8, 18)],
    ["25 9619957", "12bdc6adbb62303bcfce61f97262247fad069338554b40da818c1c22efa7e871155e658b0fa05df498cdc", get_random_int(8, 18)],
    ["25 9619950", "2e64cfd55d385d2b495f440ee8a148dec0996f5c88acd3f219ca7f6574e25c6d33fd5855a09826e2aabb5", get_random_int(8, 18)],

    ["25 7603212", "92ecfbcfdd5deccad0e5e7054270b9ac864b24c9a898b801d70ad4fe3f4901c29b0eed5d52ffae4fc65e6", get_random_int(8, 18)],
    ["25 7653589", "8a8ebc443e258aeb9d24ac1fe98a868d7ad5b4ed3f91b9661b1cfcdf08758e167bd5e2b3cd5703d2d29ed", get_random_int(8, 18)],
    ["25 7647262", "350da5697a3b19f7b2d6017cfb42653a102da2f2bde2168e5a9e7f9dd3dcfdffe856e3bb586be6a465aac", get_random_int(8, 18)],
    ["25 7617233", "860556d89c35d67978f28b51e2a0fe9a2ef85c3fac57674cb578b06acb3d3f68331688f531862a1535405", get_random_int(8, 18)],
    ["25 7628934", "a36441eb0265578fc29fb79ca2038fce7e5f24a462003d4f3cc06b57d408cea3b01f533c9f97b77289869", get_random_int(8, 18)],

    ["25 7329516", "edbc11dc8e45a426c778d9242deea09cd6c1f2a6aa42e66ca6c4d48573dc726d63dbb94c18cbcd7cc53d9", get_random_int(8, 18)],
    ["25 7559314", "af9b06edf0d78f6857b6ea54de3341dd8814313aa4049b38451423f5bc01eb1387fdc2c05ac111e95e171", get_random_int(8, 18)],
    ["25 7537018", "432881bc50e840b503f9708cee4806d37f0ad0f0a4e90a8f8eba2439ed1f6651e41dae79e2ef23a7ef75b", get_random_int(8, 18)],
    ["25 7422821", "a8fa386ca7bf64908c60c007672cb6a9509c8790344ff8165f227edf1dfb44de171d1076423e8d4fd4af9", get_random_int(8, 18)],
    ["25 7390452", "6eb5edc6b351a44970c3633f35ec295745b9d79daf28083beb1f289d56c8124c1a0c8afd675746a38740c", get_random_int(8, 18)],

    ["25 9631419", "a0a2f633469a4dd77f065ad89fd22579c786676b92b53a3603a92aee573cf0ffc2ee22c0089516654a3f4", get_random_int(8, 18)],
    ["25 9631413", "353f16c4163edb1cf0efa992470b88d52ebe98c8801ff09fe82c8da26e8ea1cb69858aab5da0a77e54703", get_random_int(8, 18)],
    ["25 9631408", "c6c88a6fa7f520d8d6bfb454524645fa3d564ed96eae8ede8b7439dba9565f09241a6ae1d7056694ff29f", get_random_int(8, 18)],
    ["25 9631390", "473474c920a663d013a17f062954e6fe5c492b2f22460c51d629e6b871b83ebad231e1c6b3d9e9b34dce6", get_random_int(8, 18)]
    # ["25 9631404", "a40abe718d5dfcb4cb2a832e00e093c32bdd5440de317ddade6b3abf2b820d8118d346930d800ceb89361", get_random_int(8, 18)]

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
