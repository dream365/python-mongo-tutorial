## Make Query
---
### Query
- findOne vs find
    - findOne은 **도큐먼트**를 반환, find는 **커서 객체**를 반환
    - 하나의 도큐먼트 조회는 findOne( = find(조건).limit(1) ), 여러 도큐먼트는 find 메서드를 사용해 커서를 반복
    - 여러 도큐먼트가 조회 되는 조건에서 findOne쓰면 기본 정렬상 첫번째 반환
    
### Paging
- skip : Parameter에 들어온 숫자 만큼 조회된 정렬 data에서 제외하고 반환

- limit : Parameter에 들어온 숫자 만큼만 정렬 data에서 포함시키고 반환

- sort : Parameter에 주어진 기준으로하여 data를 정렬 
    - db.example.sort({'A': 1, 'B': -1}) : A에 대하여 오름차순 정렬을 한뒤 B에 대하여 내림차순 정렬
    
- skip, limit, sort function을 이용하여 Pagination을 구현
    - Page 1 : db.example.skip(0).limit(5).sort({'A': 1}) (A를 기준 오름차순 정렬한뒤 Item 0 ~ Item 4)를 반환
    - Page 2 : db.example.skip(5).limit(5).sort({'A': 1}) (A를 기준 오름차순 정렬한뒤 Item 5 ~ Item 9)를 반환
    
### Projection
- find 쿼리로 조회시 모든 필드가 필요없는 상황이 있음 (i.e. 회원 존재 여부 체크 시 name, password로 유저의 존재만 알면 되기때문에 모든 필드가 필요가 없음)

- find 쿼리 시 인수 하나를 더 추가하여 프로젝션을 수행할 수 있음
    - db.example.findOne({'username' : 'sewon', 'password' : 'temp'}, {'_id': 1})
    - 인수에 필요한 필드의 해시값을 1로 설정하여 쿼리

