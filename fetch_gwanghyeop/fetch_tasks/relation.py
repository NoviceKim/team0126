# CRUD 모듈 import
from crud_module import *

# CRUD 할 클래스 객체 import
from posts import Posts
from comments import Comments
from albums import Albums
from photos import Photos
from todos import Todos
from users import Users
from address import Address
from geo import Geo
from company import Company

if __name__ == '__main__':
    # posts에 save_many 실행
    # save_many_query = "insert into tbl_posts (userid, title, body) \
    #               values (%s, %s, %s)"
    #
    # save_many_params = (
    #     (1, "sunt aut facere repellat", "quia et suscipit"),
    #     (1, "qui est esse", "est rerum tempore vitae"),
    #     (1, "ea molestias quasi", "et iusto sed quo iure"),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # comments 에 save_many 실행 후, 특정 post_id를 가진 데이터 조회
    # save_many_query = "insert into tbl_comments (post_id, name, email, body) \
    #                   values (%s, %s, %s, %s)"
    #
    # save_many_params = (
    #     (1, "id labore ex", "Eliseo@gardner.biz", "laudantium enim quasi est"),
    #     (2, "et fugit eligendi", "Presley.Mueller@myrl.com", "doloribus at sed quis"),
    #     (3, "fugit labore quia", "Veronica_Goodwin@timmothy.net", "ut dolorum nostrum"),
    # )
    #
    # save_many(save_many_query, save_many_params)
    
    # # 특정 post_id를 가진 데이터 조회
    # find_all_by_query = "select * from tbl_users where id = %s"
    # find_all_by_params = 2
    #
    # result = find_all_by(find_all_by_query, find_all_by_params)
    #
    # print(result)

    # tbl_albums 에 save_many 실행 하고 특정 userid 를 가진 데이터 update 해보기
    # save_many_query = "insert into tbl_albums (userid, title) \
    #               values (%s, %s)"
    #
    # save_many_params = (
    #   (1, "distinctio laborum qui"),
    #   (2, "quam nostrum impedit mollitia quod et dolor"),
    #   (3, "et rem non provident vel ut"),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # 특정 userid를 가진 데이터의 title에 update 실행
    # new_content = input("원하는 내용을 입력해주세요: ")
    # new_id = int(input("원하는 번호를 입력해주세요: "))
    #
    # update_query = "update tbl_albums set title = %s \
    #                 where userid = %s"
    #
    # update_params = (new_content, new_id)
    #
    # update(update_query, update_params)

    # photos 테이블에서 특정 요소 delete 실행
    # save_many_query = "insert into tbl_photos (album_id, title, url, thumbnail_url) \
    #                    values (%s, %s, %s, %s)"
    #
    # save_many_params = (
    #     (1, "사진 1", "주소 1", "https://via.placeholder.com/600/92c952"),
    #     (2, "사진 2", "주소 2", "https://via.placeholder.com/600/771796"),
    #     (3, "사진 3", "주소 3", "https://via.placeholder.com/600/56a8c2"),
    #     (4, "사진 4", "주소 4", "https://via.placeholder.com/600/66b7d2"),
    #     (5, "사진 5", "주소 5", "https://via.placeholder.com/600/fdf73e"),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # 입력값보다 큰 album_id를 가진 요소 삭제
    # delete_input = int(input("입력값보다 더 큰 album_id를 가진 요소가 삭제됩니다: "))
    #
    # delete_query = "delete from tbl_photos where album_id > %s"
    # delete_params = delete_input
    #
    # delete(delete_query, delete_params)

    # todos 테이블에서 completed가 true 인 요소만 조회
    # save_many_query = "insert into tbl_todos (userid, title, completed) \
    #                    values (%s, %s, %s)"
    #
    # save_many_params = (
    #     (1, "제목 1", True),
    #     (2, "제목 2", False),
    #     (3, "제목 3", False),
    #     (4, "제목 4", True),
    #     (5, "제목 5", True),
    #     (6, "제목 6", False),
    #     (7, "제목 7", True),
    # )
    #
    # save_many(save_many_query, save_many_params)

    # completed가 true인 모든 요소의 전체 내용 조회
    # find_all_by_query = "select * from tbl_todos where completed = %s"
    #
    # # completed가 true = 1 (bool 타입이라 그런 듯...)
    # find_all_by_params = 1
    #
    # # 결과값을 변수에 저장
    # todo_lists = find_all_by(find_all_by_query, find_all_by_params)
    #
    # # 각 줄에 출력
    # for todos in todo_lists:
    #     print(todos)

    # users 테이블에 데이터 추가한 뒤, CRUD 진행 - users, address, geo, company에 데이터 넣어야 됨
    # users 테이블부터 데이터 추가
    # 이하의 모튼 테이블의 id가 users 테이블의 FK이므로 join은 그걸 바탕으로 할 것
    # save_many_on_users_query = "insert into tbl_users (name, username, email, phone, website) \
    #                             values (%s, %s, %s, %s, %s)"
    #
    # save_many_on_users_params = (
    #     ("김광협", "KGH", "kgh1234@test.com", "01012341234", "kgh.co.kr"),
    #     ("이순신", "LSS", "lss2345@test.com", "01023456789", "lss.com"),
    #     ("장보고", "JBG", "jbg3456@test.com", "01034567890", "jbg.org"),
    #     ("허균", "HG", "hg4567@test.com", "01011111111", "hg.net"),
    #     ("장영실", "JYS", "jys5678@test.com", "01022222222", "jys.co.kr"),
    # )
    #
    # save_many(save_many_on_users_query, save_many_on_users_params)

    # address 테이블에도 내용 추가
    # save_many_on_address_query = "insert into tbl_address (street, suite, city, zipcode) \
    #                               values (%s, %s, %s, %s)"
    #
    # save_many_on_address_params = (
    #     ("회안대로", "123-4", "경기도 광주시", "123-456"),
    #     ("경충대로", "45-67", "경기도 광주시", "456-78"),
    #     ("내발산로", "567-8", "서울특별시 송파구", "345-67"),
    #     ("광안대로", "78-9", "부산광역시", "111-234"),
    #     ("상암로", "10-11", "서울특별시 강북구", "234-45"),
    # )
    #
    # save_many(save_many_on_address_query, save_many_on_address_params)

    # geo 테이블 내용 추가
    # save_many_on_geo_query = "insert into tbl_geo (lat, lng) \
    #                            values (%s, %s)"
    #
    # save_many_on_geo_params = (
    #     ("37.2", "81"),
    #     ("35", "122"),
    #     ("61.4", "21.8"),
    #     ("15.4", "23.45"),
    #     ("46.7", "77"),
    # )
    #
    # save_many(save_many_on_geo_query, save_many_on_geo_params)

    # company 테이블 내용 추가
    # save_many_on_company_query = "insert into tbl_company (name, catch_phrase, bs) \
    #                               values(%s, %s, %s)"
    #
    # save_many_on_company_params = (
    #     ("하나어패럴", "내 몸인 것처럼 편안한 옷", "bs 1"),
    #     ("두리물산", "가족같은 기업", "bs 2"),
    #     ("삼성", "최고의 클래스", "bs 3"),
    #     ("광주시청", "시민과 함께", "bs 4"),
    #     ("버거킹", "Flame Grilled since 1954", "bs 5"),
    # )
    #
    # save_many(save_many_on_company_query, save_many_on_company_params)

    # 위에서 추가한 데이터들을 바탕으로 테이블 간 join 실행
    find_all_query = "select * from tbl_users u join tbl_address a on u.id = a.id \
                      join tbl_geo g on a.id = g.id \
                      join tbl_company c on c.id = u.id"

    # 조회 결과(list 안 dict 형태)를 변수에 할당
    user_infos = find_all(find_all_query)

    # for user in user_infos:
    #     print(user)

    # user_info의 각 인덱스 안 요소(dict) 출력
    for user in user_infos:
        # user는 dict 형태의 데이터 - 따라서 .get을 사용해서 키값을 불러올 수 있음
        # 위 방법으로 출력에 사용할 문장 서식을 완성
        user_formatting = f"회원 번호: {user.get('id')} \
                            \n이름: {user.get('name')} / 유저네임: {user.get('username')} \
                            \nemail: {user.get('email')} / 전화번호: {user.get('phone')} / website: {user.get('website')} \
                            \n도로명: {user.get('street')} / 지번: {user.get('suite')} \
                            \n소재지: {user.get('city')} / 우편번호: {user.get('zipcode')} \
                            \n위도: {user.get('lat')} / 경도: {user.get('lng')} \
                            \n회사명: {user.get('c.name')} / 캐치프레이즈: {user.get('catch_phrase')} / BS: {user.get('bs')}\n"

        print(user_formatting)

