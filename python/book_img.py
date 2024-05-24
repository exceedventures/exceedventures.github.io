import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 색상 설정
chocolate_brown = '#4B3A2F'
cream = '#FFFDD0'
beige = '#F5F5DC'
gold = '#FFD700'
light_gray = '#D3D3D3'

# 캔버스 설정
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor(chocolate_brown)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# 책 커버
book_cover = patches.Rectangle((2, 2), 6, 6, linewidth=1, edgecolor=light_gray, facecolor=cream)
ax.add_patch(book_cover)

# 책 제목
plt.text(5, 6.5, 'Calm Moments', ha='center', va='center', fontsize=20, color=gold, fontweight='bold')

# 책 저자
plt.text(5, 5.5, 'by Exceed Ventures', ha='center', va='center', fontsize=12, color=light_gray)

# 책 중앙의 일러스트
plt.text(5, 4.5, '📚', ha='center', va='center', fontsize=50, color=beige)

# 바닥에 있는 그림자 효과
shadow = patches.Rectangle((2.1, 1.9), 6, 0.1, linewidth=0, edgecolor='none', facecolor=light_gray)
ax.add_patch(shadow)

plt.show()