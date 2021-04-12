"""Task 2."""
import sqlite3


class TableData:
    """Class to represent single table data from sqlite."""

    def __init__(self, database_name: str, table_name: str):
        self.table_name = table_name
        self.database_name = database_name

    def __len__(self) -> int:
        """Amount of rows in given table."""
        self._cursor.execute(f"select count(*) from {self.table_name}")
        return self._cursor.fetchone()[0]

    def __getitem__(self, item: str):
        """Get item protocol.

        Get us access to single data row for president with given name
        Example: presidents['Yeltsin'] # ('Yeltsin', 999, 'Russia')
        """
        _sql_call = f"SELECT * from {self.table_name} where name=:name"
        self._cursor.execute(_sql_call, {"name": item})
        return dict(self._cursor.fetchone())

    def __iter__(self):
        """Implement iter protocol.

        Let us iterate through the rows.
        """
        for row in self._cursor.execute(f"SELECT * from {self.table_name}"):
            yield dict(row)

    def __contains__(self, item: str) -> bool:
        """Implement contains protocol.

        Checks if given item in the given table.
        """
        _sql_call = f"SELECT EXISTS(SELECT 1 from {self.table_name} where name=:name)"
        self._cursor.execute(_sql_call, {"name": item})
        return self._cursor.fetchone()[0]

    def __enter__(self):
        """Context manager enter."""
        self._conn = sqlite3.connect(self.database_name)
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # noqa: ANN001
        """Context manager exit."""
        self._conn.close()
