# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Mark implied non-nullable fields as non-nullable

Revision ID: 92e08fe9032b
Revises: 87509f4ae027
Create Date: 2020-08-10 20:12:46.392075
"""

import sqlalchemy as sa

from alembic import op
from sqlalchemy.dialects import postgresql

revision = "92e08fe9032b"
down_revision = "87509f4ae027"


def upgrade():
    op.alter_column(
        "release_files", "comment_text", existing_type=sa.TEXT(), nullable=False
    )
    op.alter_column(
        "release_files", "filename", existing_type=sa.TEXT(), nullable=False
    )
    op.alter_column(
        "release_files", "has_signature", existing_type=sa.BOOLEAN(), nullable=False
    )
    op.alter_column(
        "release_files",
        "packagetype",
        existing_type=postgresql.ENUM(
            "bdist_dmg",
            "bdist_dumb",
            "bdist_egg",
            "bdist_msi",
            "bdist_rpm",
            "bdist_wheel",
            "bdist_wininst",
            "sdist",
            name="package_type",
        ),
        nullable=False,
    )
    op.alter_column(
        "release_files", "python_version", existing_type=sa.TEXT(), nullable=False
    )
    op.alter_column("release_files", "size", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column(
        "release_files",
        "upload_time",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
        existing_server_default=sa.text("now()"),
    )


def downgrade():
    op.alter_column(
        "release_files",
        "upload_time",
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
        existing_server_default=sa.text("now()"),
    )
    op.alter_column("release_files", "size", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column(
        "release_files", "python_version", existing_type=sa.TEXT(), nullable=True
    )
    op.alter_column(
        "release_files",
        "packagetype",
        existing_type=postgresql.ENUM(
            "bdist_dmg",
            "bdist_dumb",
            "bdist_egg",
            "bdist_msi",
            "bdist_rpm",
            "bdist_wheel",
            "bdist_wininst",
            "sdist",
            name="package_type",
        ),
        nullable=True,
    )
    op.alter_column(
        "release_files", "has_signature", existing_type=sa.BOOLEAN(), nullable=True
    )
    op.alter_column("release_files", "filename", existing_type=sa.TEXT(), nullable=True)
    op.alter_column(
        "release_files", "comment_text", existing_type=sa.TEXT(), nullable=True
    )
