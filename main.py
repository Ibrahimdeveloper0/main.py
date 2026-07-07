import flet as ft
import random

def main(page: ft.Page):
    # Mobil telefon ölçüləri və dizayn tənzimləmələri
    page.title = "Halı Saha Takım Bölüştürücü"
    page.window_width = 380
    page.window_height = 700
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "adaptive"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 15

    # =========================================================================
    # SİSTEM 1: BÜTÜN OYUNÇULARI BİRDƏN BÖLMƏK (Sənin 1-ci kod məntiqin)
    # =========================================================================
    s1_oyuncular = []
    
    s1_input = ft.TextField(label="Oyunçu Adı", width=200, border_color=ft.Colors.GREEN_400)
    s1_liste_txt = ft.Text("Əlavə olunan oyunçular: Yoxdur", italic=True, size=12)
    s1_takim_a = ft.Column(spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    s1_takim_b = ft.Column(spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def s1_oyuncu_ekle(e):
        if s1_input.value.strip():
            s1_oyuncular.append(s1_input.value.strip())
            s1_liste_txt.value = f"Əlavə olunan oyunçular: {', '.join(s1_oyuncular)}"
            s1_input.value = ""
            page.update()

    def s1_bolustur(e):
        if len(s1_oyuncular) < 2:
            return
        
        # SƏNİN KODUNDAKI 1-Cİ ALQORİTM:
        z = s1_oyuncular.copy()
        a = []
        s = len(z)
        for i in range(s // 2):
            chose = random.choice(z)
            a.append(chose)
            z.remove(chose)
        b = z

        # Ekranda göstərmək
        s1_takim_a.controls = [ft.Text("🟢 A KOMANDASI", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_300)] + [ft.Text(o) for o in a]
        s1_takim_b.controls = [ft.Text("🔴 B KOMANDASI", weight=ft.FontWeight.BOLD, color=ft.Colors.RED_300)] + [ft.Text(o) for o in b]
        page.update()

    sistem_1_view = ft.Column([
        ft.Text("🏟️ SİSTEM 1: TOPLU BÖLÜŞDÜRMƏ", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_400),
        ft.Row([
            s1_input, 
            ft.ElevatedButton(content=ft.Text("Əlavə et"), on_click=s1_oyuncu_ekle, bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE)
        ], alignment=ft.MainAxisAlignment.CENTER),
        s1_liste_txt,
        ft.Divider(),
        ft.ElevatedButton(content=ft.Text("Komandalara Böl"), on_click=s1_bolustur, width=250, bgcolor=ft.Colors.GREEN_600, color=ft.Colors.WHITE),
        ft.Divider(),
        ft.Row([
            ft.Container(content=s1_takim_a, padding=10, bgcolor=ft.Colors.BLACK26, border_radius=10, width=150),
            ft.Container(content=s1_takim_b, padding=10, bgcolor=ft.Colors.BLACK26, border_radius=10, width=150)
        ], alignment=ft.MainAxisAlignment.CENTER)
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=True)

    # =========================================================================
    # SİSTEM 2: İKİŞƏR SEÇİB RANDOM ATMAQ (Sənin 2-ci kod məntiqin)
    # =========================================================================
    s2_takim_a_list = []
    s2_takim_b_list = []

    s2_input_1 = ft.TextField(label="1-ci Oyunçu", width=140, border_color=ft.Colors.BLUE_400)
    s2_input_2 = ft.TextField(label="2-ci Oyunçu", width=140, border_color=ft.Colors.BLUE_400)
    
    s2_takim_a_ui = ft.Column(spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    s2_takim_b_ui = ft.Column(spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def s2_secim_yap(e):
        vv = s2_input_1.value.strip()
        vvv = s2_input_2.value.strip()
        
        if vv and vvv:
            # SƏNİN KODUNDAKI 2-Cİ ALQORİTM:
            dol = [vv, vvv]
            secim = random.choice(dol)
            
            s2_takim_a_list.append(secim)
            dol.remove(secim)
            s2_takim_b_list.append(dol[0]) # List daxilindən birbaşa mətni götürürük
            
            # İnputları təmizləyirik
            s2_input_1.value = ""
            s2_input_2.value = ""
            
            # Ekranı yeniləyirik
            s2_takim_a_ui.controls = [ft.Text("🟢 A KOMANDASI", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_300)] + [ft.Text(o) for o in s2_takim_a_list]
            s2_takim_b_ui.controls = [ft.Text("🔴 B KOMANDASI", weight=ft.FontWeight.BOLD, color=ft.Colors.RED_300)] + [ft.Text(o) for o in s2_takim_b_list]
            page.update()

    sistem_2_view = ft.Column([
        ft.Text("🤝 SİSTEM 2: 2-ŞƏR OYUNÇU SEÇMƏ", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_400),
        ft.Row([s2_input_1, s2_input_2], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(height=10),
        ft.ElevatedButton(content=ft.Text("Təsadüfi Komandaya Dağıt"), on_click=s2_secim_yap, width=250, bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE),
        ft.Divider(),
        ft.Row([
            ft.Container(content=s2_takim_a_ui, padding=10, bgcolor=ft.Colors.BLACK26, border_radius=10, width=150),
            ft.Container(content=s2_takim_b_ui, padding=10, bgcolor=ft.Colors.BLACK26, border_radius=10, width=150)
        ], alignment=ft.MainAxisAlignment.CENTER)
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)

    # =========================================================================
    # SİSTEMLƏR ARASI SAYFA GEÇİŞİ (TƏK DÜYMƏ MƏNTİQİ)
    # =========================================================================
    def sistem_degistir(e):
        if sistem_1_view.visible:
            sistem_1_view.visible = False
            sistem_2_view.visible = True
            gecis_butonu.content = ft.Text("🔄 Toplu Bölüşdürməyə Keç")
            gecis_butonu.bgcolor = ft.Colors.GREEN_700
        else:
            sistem_1_view.visible = True
            sistem_2_view.visible = False
            gecis_butonu.content = ft.Text("🔄 2-şər Seçməyə Keç")
            gecis_butonu.bgcolor = ft.Colors.BLUE_700
        page.update()

    gecis_butonu = ft.ElevatedButton(
        content=ft.Text("🔄 2-şər Seçməyə Keç"), 
        on_click=sistem_degistir, 
        bgcolor=ft.Colors.BLUE_700, 
        color=ft.Colors.WHITE,
        width=280
    )

    # Ekrana əlavə etmə
    page.add(
        ft.Container(height=10),
        gecis_butonu,
        ft.Container(height=20),
        sistem_1_view,
        sistem_2_view
    )

if __name__ == "__main__":
    ft.app(target=main)
