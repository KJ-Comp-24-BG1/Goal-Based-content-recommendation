from django import forms

PLATFORMS = [
    ('edx', 'EdX'),
    ('skillshare', 'Skillshare'),
    ('coursera', 'Coursera'),
    ('udemy', 'Udemy'),
]

class GoalForm(forms.Form):
    goal = forms.CharField(label='Your Goal', max_length=255, required=True)
    platforms = forms.MultipleChoiceField(label='Select Platforms', choices=PLATFORMS, required=True, widget=forms.CheckboxSelectMultiple)