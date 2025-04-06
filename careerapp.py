from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout


career_data = {
    "Higher Studies (M.Sc, MBA)": {"salary": "₹25,000–₹80,000", "hours": "6–8 hrs", "stress": "Moderate"},
    "Competitive Exams (UPSC, NET, GATE)": {"salary": "₹50,000–₹1,20,000", "hours": "8–12 hrs", "stress": "High"},
    "Research & Development (R&D)": {"salary": "₹35,000–₹1,00,000", "hours": "8–9 hrs", "stress": "Moderate to High"},
    "Industry Jobs": {"salary": "₹20,000–₹90,000", "hours": "8–10 hrs", "stress": "Moderate"},
    "Entrepreneurship": {"salary": "Variable", "hours": "10+ hrs", "stress": "High"},
    "Teaching & Academia": {"salary": "₹20,000–₹60,000", "hours": "6–8 hrs", "stress": "Low to Moderate"},
    "Science Communication": {"salary": "₹10,000–₹1,00,000+", "hours": "Flexible", "stress": "Low to Moderate"}
}

criteria = {
    "Interest Level": "Excitement?",
    "Job Security": "Stability?",
    "Salary Potential": "Financial growth?",
    "Growth Opportunity": "Learning chances?",
    "Work-Life Balance": "Personal vs. professional?"
}


class CareerApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        scroll = ScrollView()
        self.grid = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))

        self.ratings = {}

        for career, details in career_data.items():
            card = BoxLayout(orientation='vertical', size_hint_y=None, height=350, padding=10, spacing=5)
            card.add_widget(Label(text=f"[b]{career}[/b]", markup=True, font_size=18, size_hint_y=None, height=30))
            card.add_widget(Label(text=f"💸 Salary: {details['salary']}", font_size=14, size_hint_y=None, height=25))
            card.add_widget(Label(text=f"🕒 Working Hours: {details['hours']}", font_size=14, size_hint_y=None, height=25))
            card.add_widget(Label(text=f"😰 Stress Level: {details['stress']}", font_size=14, size_hint_y=None, height=25))

            self.ratings[career] = {}
            for crit in criteria:
                row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                row.add_widget(Label(text=f"{crit}:", size_hint_x=0.5))
                spinner = Spinner(text='3', values=[str(i) for i in range(1, 6)], size_hint_x=0.3)
                self.ratings[career][crit] = spinner
                row.add_widget(spinner)
                card.add_widget(row)

            self.grid.add_widget(card)

        scroll.add_widget(self.grid)

        submit_btn = Button(
            text="🎯 Show Best Career Option",
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.7, 0.3, 1),
            font_size=18,
            on_press=self.calculate_result
        )

        root.add_widget(scroll)
        root.add_widget(submit_btn)

        return root

    def calculate_result(self, instance):
        scores = {}
        for career in self.ratings:
            total = sum(int(self.ratings[career][crit].text) for crit in criteria)
            scores[career] = total

        best_career = sorted(scores.items(), key=lambda x: x[1], reverse=True)[0][0]
        info = career_data[best_career]

        result = f"""
🌟 Best Match: {best_career}

💸 Salary: {info['salary']}
🕒 Hours: {info['hours']}
😰 Stress: {info['stress']}
        """

        popup = Popup(
            title='🌈 Your Career Recommendation',
            content=Label(text=result.strip()),
            size_hint=(0.85, 0.6)
        )
        popup.open()


if __name__ == '__main__':
    CareerApp().run()
