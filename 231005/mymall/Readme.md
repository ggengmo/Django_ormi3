```
쇼핑몰을 만들 예정입니다. 쇼핑몰에 만들 url 목록은 아래와 같습니다. 

'index' => 잘 나가는 상품 10개 소개
'/about' => 회사 소개
'/product' => 상품 목록
'/product/1'=> 상품 목록 상세 게시물
'/contact' => 오시는 길
'/qna' => Q&A 목록
'/qna/1'=> Q&A 상세 게시물
'/notice' => 자유게시판, 1:1게시판 선택 페이지
'/notice/free' => 자유게시판 목록
'/notice/free/1' => 자유게시판 상세 게시물
'/notice/onenone' => 1:1 상담 안내
'/notice/onenone/1'  => 1:1 상담 상세 게시물

앱이름:main         views 함수이름    html 파일이름    비고
''  			          index		         index.html      
'about/' 		        about		         about.html       
'contact/'		      contact		       contact.html

앱이름:prduct        views 함수이름    html 파일이름    비고
'product/'		       product		      product.html
'product/<int:pk>'   post            	post.html

앱이름:qna        views 함수이름    html 파일이름    비고
'qna/'			      qna		           qna.html
'qna/<int:pk>'    post        	   post.html

앱이름:notice               views 함수이름    html 파일이름    비고
'notice/'		                notice		       notice.html
'notice/free'		            free		         free.html
'notice/free/<int:pk>'	    free_detail	     free_detail.html
'notice/onenone'	          onenone		       onenone.html
'notice/onenone/<int:pk>'   onenone.detail	 onenone.detail.html
-------------------------------------------------------

```
