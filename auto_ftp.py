import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server():
    # FTP 접근 권한 설정
    authorizer = DummyAuthorizer()

    # 익명 사용자 추가 (아이디/비밀번호 없음)
    ftp_root = "/data"  # FTP 서버 루트 디렉토리
    if not os.path.exists(ftp_root):
        os.makedirs(ftp_root)  # 디렉토리가 없으면 생성
    authorizer.add_anonymous(ftp_root, perm='elradfmw')  # 읽기, 쓰기 권한 포함

    # FTP 핸들러 설정
    handler = FTPHandler
    handler.authorizer = authorizer

    # FTP 서버 설정 (2121 포트)
    server = FTPServer(("0.0.0.0", 2121), handler)
    print(f"FTP 서버가 포트 2121에서 실행 중입니다. 루트: {ftp_root}")

    # 서버 시작
    server.serve_forever()

if __name__ == "__main__":
    start_ftp_server()
