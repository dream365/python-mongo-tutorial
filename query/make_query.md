## Make Query
---
### Query
- findOne vs find
    - findOne은 **도큐먼트**를 반환, find는 **커서 객체**를 반환
    - 하나의 도큐먼트 조회는 findOne( = find(조건).limit(1) ), 여러 도큐먼트는 find 메서드를 사용해 커서를 반복
    - 여러 도큐먼트가 조회 되는 조건에서 findOne쓰면 기본 정렬상 첫번째 반환