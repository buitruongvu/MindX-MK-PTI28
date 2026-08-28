import operator
from datetime import datetime

class AnimeItem:
    def __init__(self, anime_id, title, release_date, image=None, rating=None, link=None):
        self.id = anime_id
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = float(rating) if rating else 0.0
        self.link = link

    def update(self, new_data: dict):
        for attribute, value in new_data.items():
            if value:
                setattr(self, attribute, value)

class AnimeList:
    def __init__(self):
        self.anime_item_list = list()

    def get_first_item_by_title(self, anime_title):
        for anime_item in self.anime_item_list:
            if anime_item.title == anime_title:
                return anime_item
        return False

    def add_item(self, anime_dict):
        """Đã sửa lại dùng .get() để tránh lỗi KeyError"""
        anime_dict["id"] = len(self.anime_item_list)
        new_item = AnimeItem(
            anime_id=anime_dict["id"], 
            title=anime_dict.get("title", "Unknown"), 
            release_date=anime_dict.get("release_date", "Jan 1970"), 
            image=anime_dict.get("image"), 
            rating=anime_dict.get("rating"), 
            link=anime_dict.get("link")
        )
        self.anime_item_list.append(new_item)

    def edit_item(self, edit_title, new_dict):
        matched = self.get_first_item_by_title(edit_title)
        if matched:
            matched.update(new_dict)

    def delete_item(self, delete_title):
        matched = self.get_first_item_by_title(delete_title)
        if matched:
            self.anime_item_list.remove(matched)

    def search_by_title(self, search_title) -> list[AnimeItem]:
        matched_items = []
        for anime_item in self.anime_item_list:
            if search_title.lower() in anime_item.title.lower():
                matched_items.append(anime_item)
        return matched_items

    def sort_item_by_rating(self, top=None):
        self.anime_item_list = sorted(self.anime_item_list, key=operator.attrgetter('rating'), reverse=True)
        return self.anime_item_list[:top] if top else self.anime_item_list

    def sort_item_by_title(self, top=None):
        self.anime_item_list = sorted(self.anime_item_list, key=operator.attrgetter('title'), reverse=True)
        return self.anime_item_list[:top] if top else self.anime_item_list
  
    def sort_item_by_date(self, top=None):
        self.anime_item_list = sorted(self.anime_item_list, key=lambda x: format_date(x.release_date), reverse=True)
        return self.anime_item_list[:top] if top else self.anime_item_list
  
def format_date(date_text):
    try:
        return datetime.strptime(date_text, '%b %Y')
    except ValueError:
        return datetime.min # Tránh lỗi nếu user nhập sai format ngày tháng


# --- HÀM HỖ TRỢ IN DANH SÁCH ---
def print_anime_list(header_text, anime_list):
    print(f"\n{'='*10} {header_text.upper()} {'='*10}")
    if not anime_list:
        print("Danh sách trống hoặc không tìm thấy kết quả!")
        return
        
    print(f"{'ID':<3} | {'Title':<20} | {'Release Date':<15} | {'Rating':<6}")
    print("-" * 55)
    for anime in anime_list:
        title = anime.title if anime.title else "N/A"
        date = anime.release_date if anime.release_date else "N/A"
        print(f"{anime.id:<3} | {title:<20} | {date:<15} | {anime.rating:<6}")
    print("=" * 55)


# --- MENU TƯƠNG TÁC (CLI) ---
def interactive_menu():
    my_list = AnimeList()
    
    # Thêm sẵn vài data để đỡ phải gõ tay từ đầu
    my_list.add_item({"title": "Naruto", "release_date": "Oct 2002", "rating": 8.3})
    my_list.add_item({"title": "One Piece", "release_date": "Oct 1999", "rating": 8.9})

    while True:
        print("\n" + "="*30)
        print("    QUẢN LÝ DANH SÁCH ANIME")
        print("="*30)
        print("1. Thêm Anime mới")
        print("2. Xóa Anime")
        print("3. Xem danh sách (Sắp xếp theo Rating)")
        print("4. Tìm kiếm Anime")
        print("0. Thoát chương trình")
        
        choice = input("👉 Nhập lựa chọn của bạn (0-4): ")

        if choice == '1':
            print("\n--- THÊM ANIME ---")
            title = input("Tên Anime: ")
            date = input("Ngày phát hành (VD: Oct 2020): ")
            rating_input = input("Rating (Nhập số hoặc để trống): ")
            
            new_data = {
                "title": title,
                "release_date": date,
                "rating": float(rating_input) if rating_input.strip() else None
            }
            my_list.add_item(new_data)
            print(f"✅ Đã thêm '{title}' thành công!")

        elif choice == '2':
            print("\n--- XÓA ANIME ---")
            title = input("Nhập tên Anime cần xóa: ")
            # Kiểm tra xem có tồn tại không trước khi xóa
            if my_list.get_first_item_by_title(title):
                my_list.delete_item(title)
                print(f"✅ Đã xóa '{title}'!")
            else:
                print(f"❌ Không tìm thấy Anime tên '{title}'.")

        elif choice == '3':
            # Vừa xem vừa sắp xếp rating cho đẹp
            sorted_list = my_list.sort_item_by_rating()
            print_anime_list("DANH SÁCH ANIME", sorted_list)

        elif choice == '4':
            print("\n--- TÌM KIẾM ---")
            keyword = input("Nhập từ khóa tìm kiếm: ")
            results = my_list.search_by_title(keyword)
            print_anime_list(f"KẾT QUẢ CHO '{keyword}'", results)

        elif choice == '0':
            print("\n👋 Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    # Chạy menu thay vì mock data tĩnh
    interactive_menu()