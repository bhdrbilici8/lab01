{% extends "base.html" %}
{% block content %}
<div class="form-page">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-7 col-lg-6">

        <nav aria-label="breadcrumb" class="mb-3">
          <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="{{ url_for('main.books') }}">Books</a></li>
            <li class="breadcrumb-item active">Add New Book</li>
          </ol>
        </nav>

        <div class="form-card">
          <div class="form-card-header">
            <h2 class="form-card-title">
              <i class="bi bi-book-half me-2"></i>Add a New Book
            </h2>
            <p class="text-muted mb-0">Share a book with the Folio community</p>
          </div>

          <form method="POST" novalidate>
            {{ form.hidden_tag() }}

            <div class="mb-3">
              {{ form.title.label(class="form-label fw-medium") }}
              {{ form.title(class="form-control" + (" is-invalid" if form.title.errors else ""),
                            placeholder="e.g. The Great Gatsby") }}
              {% for e in form.title.errors %}
              <div class="invalid-feedback">{{ e }}</div>
              {% endfor %}
            </div>

            <div class="mb-3">
              {{ form.author.label(class="form-label fw-medium") }}
              {{ form.author(class="form-control" + (" is-invalid" if form.author.errors else ""),
                             placeholder="e.g. F. Scott Fitzgerald") }}
              {% for e in form.author.errors %}
              <div class="invalid-feedback">{{ e }}</div>
              {% endfor %}
            </div>

            <div class="mb-4">
              {{ form.description.label(class="form-label fw-medium") }}
              {{ form.description(class="form-control" + (" is-invalid" if form.description.errors else ""),
                                  rows=5, placeholder="Short description or synopsis…") }}
              {% for e in form.description.errors %}
              <div class="invalid-feedback">{{ e }}</div>
              {% endfor %}
            </div>

            <div class="d-flex gap-2">
              {{ form.submit(class="btn btn-accent flex-grow-1") }}
              <a href="{{ url_for('main.books') }}" class="btn btn-outline-secondary">Cancel</a>
            </div>
          </form>
        </div>

      </div>
    </div>
  </div>
</div>
{% endblock %}
