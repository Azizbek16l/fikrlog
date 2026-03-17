from articles import Article
import pytest

@pytest.fixture
def article():
    return Article('Test title')

def test_Articles_init(article):
    
    assert article.title=='Test title'
    assert article.content==""
    
def test_article_slug(article):
    
    assert article.slug == "test-title"
    

def test_article_slug_mock(mocker, article):
    # given
    mock_slugify=mocker.patch('articles.slugify', return_value="slug")
    a=Article("Test title")
    # when
    got= article.slug
    
    # then
    assert got == "slug"
    mock_slugify.assert_called()