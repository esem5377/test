import math

# 입력
f = float(input("주파수 f(Hz)를 입력하세요 : "))
a_mm = float(input("내부도체 반지름 a(mm)를 입력하세요 : "))
b_mm = float(input("외부도체 안쪽 반지름 b(mm)를 입력하세요 : "))
er = float(input("비유전율 er를 입력하세요 : "))
tan_d = float(input("tanδ를 입력하세요 : "))
sigma = float(input("도전율 σ(S/m)를 입력하세요 : "))

# 단위 변환 (mm -> m)
a = a_mm * 1e-3
b = b_mm * 1e-3

# 상수
mu0 = 4 * math.pi * 1e-7          
eps0 = 8.854e-12                  
mur = 1.0

# 기본 파라미터
mu = mu0 * mur
eps_p = er * eps0                 
eps_pp = er * eps0 * tan_d        
omega = 2 * math.pi * f

# 표면저항
Rs = math.sqrt(math.pi * f * mu0 / sigma)

# ln(b/a)
ln_ba = math.log(b / a)

# 전송선로 파라미터
L = (mu / (2 * math.pi)) * ln_ba
C = (2 * math.pi * eps_p) / ln_ba
R = (Rs / (2 * math.pi)) * ((1 / a) + (1 / b))
G = (2 * math.pi * omega * eps_pp) / ln_ba

# 특성 임피던스
Z0 = math.sqrt(L / C)
Y0 = 1 / Z0

# 감쇠정수
alpha_c = R / (2 * Z0)
alpha_d = G / (2 * Y0)
alpha = alpha_c + alpha_d

# dB/m 변환
alpha_c_db = 8.686 * alpha_c
alpha_d_db = 8.686 * alpha_d
alpha_db = 8.686 * alpha

# 위상정수와 유도파장
beta = omega * math.sqrt(L * C)
lambda_g = (2 * math.pi) / beta

# 출력
print("\n[계산 결과]")
print(f"Z0 = {Z0:.6f} ohm")
print(f"R  = {R:.6e} ohm/m")
print(f"L  = {L:.6e} H/m")
print(f"C  = {C:.6e} F/m")
print(f"G  = {G:.6e} S/m")
print(f"alpha_c = {alpha_c_db:.6f} dB/m")
print(f"alpha_d = {alpha_d_db:.6f} dB/m")
print(f"alpha   = {alpha_db:.6f} dB/m")
print(f"beta = {beta:.6f} rad/m")
print(f"lambda_g = {lambda_g:.6f} m")
