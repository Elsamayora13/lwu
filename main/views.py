from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def purchase_history_view(request):
    purchases = [
        {
            'invoice': 'INV-20260701-001',
            'item': 'Writing Task 2: Coherence & Cohesion',
            'date': 'July 1, 2026',
            'amount': 'Rp 249.000',
            'status': 'Paid',
        },
        {
            'invoice': 'INV-20260615-002',
            'item': 'IELTS Speaking Mastery: Idioms & Collocations Guide',
            'date': 'June 15, 2026',
            'amount': 'Rp 89.000',
            'status': 'Paid',
        },
        {
            'invoice': 'INV-20260530-003',
            'item': 'Advanced Reading Techniques',
            'date': 'May 30, 2026',
            'amount': 'Rp 199.000',
            'status': 'Pending',
        },
        {
            'invoice': 'INV-20260510-004',
            'item': 'Essential Grammar for IELTS',
            'date': 'May 10, 2026',
            'amount': 'Rp 149.000',
            'status': 'Failed',
        },
    ]
    return render(request, 'purchase_history.html', {
        'purchases': purchases,
        'current_page': 'purchase_history'
    })

@login_required
def course_view(request):
    courses = [
        {
            'title': 'Writing Task 2: Coherence & Cohesion',
            'category': 'Writing',
            'thumbnail': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=800',
            'progress': 65,
        },
        {
            'title': 'Speaking Mastery: IELTS Part 2',
            'category': 'Speaking',
            'thumbnail': 'https://images.unsplash.com/photo-1543269664-56d93c1b41a6?auto=format&fit=crop&q=80&w=800',
            'progress': 30,
        },
        {
            'title': 'Advanced Reading Techniques',
            'category': 'Reading',
            'thumbnail': 'https://images.unsplash.com/photo-1516321497487-e288fb19713f?auto=format&fit=crop&q=80&w=800',
            'progress': 85,
        },
        {
            'title': 'Essential Grammar for IELTS',
            'category': 'Grammar',
            'thumbnail': 'https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&q=80&w=800',
            'progress': 10,
        },
        {
            'title': 'Academic Vocabulary Booster',
            'category': 'Vocabulary',
            'thumbnail': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&q=80&w=800',
            'progress': 95,
        },
    ]
    return render(request, 'course.html', {
        'courses': courses,
        'current_page': 'course'
    })

@login_required
def ebook_view(request):
    ebooks = [
        {'title': 'IELTS Writing Bank: 100+ High-Score Sample Essays', 'size': '48 MB', 'tag': 'Learning With Us Press'},
        {'title': 'IELTS Speaking Mastery: Idioms & Collocations Guide', 'size': '14 MB', 'tag': 'Vocabulary Series'},
        {'title': 'The Ultimate Guide to IELTS Reading Comprehension', 'size': '22 MB', 'tag': 'Strategy Guide'}
    ]
    return render(request, 'ebook.html', {
        'ebooks': ebooks,
        "current_page": "ebook"
    })

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html",{
        "current_page": "dashboard",
    })