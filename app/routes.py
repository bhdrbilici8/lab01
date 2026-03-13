from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app import db
from app.models import Book, Review
from app.forms import BookForm, ReviewForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    recent_books   = Book.query.order_by(Book.created_at.desc()).limit(6).all()
    recent_reviews = Review.query.order_by(Review.created_at.desc()).limit(5).all()
    total_books    = Book.query.count()
    total_reviews  = Review.query.count()
    return render_template('index.html',
                           title='Home',
                           recent_books=recent_books,
                           recent_reviews=recent_reviews,
                           total_books=total_books,
                           total_reviews=total_reviews)


@main.route('/books')
def books():
    page      = 1
    per_page  = 12
    all_books = Book.query.order_by(Book.created_at.desc()).all()
    return render_template('books.html', title='Books', books=all_books)


@main.route('/books/<int:book_id>')
def book_detail(book_id):
    book    = Book.query.get_or_404(book_id)
    reviews = Review.query.filter_by(book_id=book_id)\
                          .order_by(Review.created_at.desc()).all()
    # Check if current user already reviewed this book
    user_reviewed = False
    if current_user.is_authenticated:
        user_reviewed = Review.query.filter_by(
            book_id=book_id, user_id=current_user.id).first() is not None
    return render_template('book_detail.html',
                           title=book.title,
                           book=book,
                           reviews=reviews,
                           user_reviewed=user_reviewed)


@main.route('/books/add', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data,
                    author=form.author.data,
                    description=form.description.data)
        db.session.add(book)
        db.session.commit()
        flash(f'"{book.title}" has been added successfully!', 'success')
        return redirect(url_for('main.book_detail', book_id=book.id))
    return render_template('add_book.html', title='Add Book', form=form)


@main.route('/books/<int:book_id>/review', methods=['GET', 'POST'])
@login_required
def add_review(book_id):
    book = Book.query.get_or_404(book_id)

    # Prevent duplicate reviews
    existing = Review.query.filter_by(book_id=book_id,
                                      user_id=current_user.id).first()
    if existing:
        flash('You have already reviewed this book.', 'warning')
        return redirect(url_for('main.book_detail', book_id=book_id))

    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(rating=form.rating.data,
                        review_text=form.review_text.data,
                        user_id=current_user.id,
                        book_id=book_id)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been submitted!', 'success')
        return redirect(url_for('main.book_detail', book_id=book_id))

    return render_template('add_review.html',
                           title='Add Review',
                           form=form,
                           book=book)
