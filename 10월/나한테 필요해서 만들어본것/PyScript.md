# PyScript

 **파이썬을 html에 적용시키는 친구다**



### 사용법

<!-- <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" /> -->

  <script defer src="https://pyscript.net/latest/pyscript.js"></script>

head에 대충 쟤들을 넣는다 (css는 로딩때문에 뺐음)

```html
<py-script> pring('hello') </py-script>
이런식으로 쓰면 기본적으로 된다
```



### 모듈 넣기

```html
<py-env></py-env> 태그 내부에 파이썬 코드를 그대로 넣으면 되는데,

모듈은 head 부분에 
<py-config>
    - random
    - Counter
</py-config>
이런식으로 추가해줘야 굴러간다.

random은 내장이라서 안넣어도되는듯..?
```



